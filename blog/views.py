# LIBRARIES
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from logging import basicConfig, DEBUG, debug, disable, CRITICAL

# FORMS
from .forms import CommentForm

# MODELS
from .models import (
    BlogPageMetaDescription,
    BlogPageBlogPost,
    BlogPageComment,
    BlogPageVisit,
    BlogPagePostDetailPageVisit,
    BlogPagePostLike,
    BlogPageShareClick,
)


# CUSTOM FUNCTIONS
from custom_functions.visitors_ip_address import get_ip
from custom_functions.visitors_user_agent import get_user_agent
from custom_functions.social_media_button_click_processor import social_media_button_click_processor
from custom_functions.document_click_coordinate_processor import document_click_coordinate_processor
from custom_functions.mouse_trace_processor import mouse_trace_processor
from custom_functions.keystroke_processor import keystroke_processor



# Configuring debugging feature code
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Disabling the debugging feature. Hint: Comment out this line to enable debugging.
# disable(CRITICAL)



##############################

# BLOG PAGE

##############################

def blog(request):
    """A view function which renders the blog page."""

    ip = get_ip(request)
    user_agent = get_user_agent(request)

    if request.POST.get("id") == "blog_page_visit_information":

        BlogPageVisit.objects.create(ip_address=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"))

    social_media_button_click_processor(request=request, id="smbci", ip=ip, user_agent=user_agent, platform_choice=request.POST.get("choice"), page_url=request.POST.get("current_url"))
    document_click_coordinate_processor(request=request, id="document_click_coordinate_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))
    mouse_trace_processor(request=request, id="mouse_trace_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))
    keystroke_processor(request=request, id="keystroke_request", ip=ip, user_agent=user_agent, keystroke=request.POST.get("key_value"), page_url=request.POST.get("current_url"))
    
    all_meta_description_objs = BlogPageMetaDescription.objects.all()
    all_blog_post_objs = BlogPageBlogPost.objects.all()

    context = {

        'all_meta_description_objs': all_meta_description_objs,
        'all_blog_post_objs': all_blog_post_objs,

    }

    return render(request, 'blog/blog.html', context=context)

def post_detail_view(request, id):
    """A view function which renders the blog detail pages"""

    context = {}

    ip = get_ip(request)
    user_agent = get_user_agent(request)

    if request.POST.get("id") == "blog_post_detail_page_visit_information":

        BlogPagePostDetailPageVisit.objects.create(ip_address=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"))

    social_media_button_click_processor(request=request, id="smbci", ip=ip, user_agent=user_agent, platform_choice=request.POST.get("choice"), page_url=request.POST.get("current_url"))
    document_click_coordinate_processor(request=request, id="document_click_coordinate_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))
    mouse_trace_processor(request=request, id="mouse_trace_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))
    keystroke_processor(request=request, id="keystroke_request", ip=ip, user_agent=user_agent, keystroke=request.POST.get("key_value"), page_url=request.POST.get("current_url"))

    if request.POST.get("id") == "send_like_post_request":

        if BlogPagePostLike.objects.filter(post=id, ip_address=ip).exists():

            debug("Object is already exists in the database so, modifying it.")
            BlogPagePostLike.objects.filter(post=id, ip_address=ip).update(like_status=request.POST.get("choice"))

        else:

            debug("Object is not exists in the database so, creating a new one.")
            BlogPagePostLike.objects.create(post_id=id,  ip_address=ip, user_agent=user_agent, like_status=request.POST.get("choice"))

    if request.POST.get("requestId") == "share_on_social_media_request":

        BlogPageShareClick.objects.create(uuid=id, ip_address=ip, user_agent=user_agent, platform_choice=request.POST.get("platformCTShare"))

    post_detail = get_object_or_404(BlogPageBlogPost, id=id)

    if BlogPagePostLike.objects.filter(post=id, ip_address=ip).exists():

        post_like_objs = BlogPagePostLike.objects.get(post=id, ip_address=ip)
        context['post_like_objs'] = post_like_objs

    post_like_count = BlogPagePostLike.objects.filter(post=id, like_status='l').count()

    if request.POST.get("id") == "delete_comment_request":

        commenter_name = request.POST.get("choice").split(' - ')[0]
        comment_time = request.POST.get("choice").split(' - ')[-1]
        BlogPageComment.objects.get(commenter_name=commenter_name, comment_time=comment_time).delete()

    comment_form = CommentForm()

    if request.method == "POST" and "commentbtn" in request.POST:

        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():

            debug(comment_form.cleaned_data)
            BlogPageComment.objects.create(commenter_name=request.user.username, text=comment_form.cleaned_data['text'], ip_address=ip, user_agent=user_agent, post_id=post_detail.id,)

        else:

            debug(comment_form.errors)

        return HttpResponseRedirect(f'/blog/{id}')

    number_of_comments = BlogPageComment.objects.filter(post=id).count()

    if post_detail.post_type == "e" and not request.user.is_authenticated:

        return HttpResponseRedirect('/login/')
        
    context['comment_form'] = CommentForm
    context['post_detail'] = post_detail
    context['post_like_count'] = post_like_count
    context['usersIp'] = ip
    context['number_of_comments'] = number_of_comments

    return render(request, 'blog/blog_post_detail.html', context=context)
