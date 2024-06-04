# LIBRARIES
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from logging import basicConfig, DEBUG, debug, disable, CRITICAL

# MODELS
from .models import (
    RegisterPageMetaDescription,
    RegisterPageVisit,

    Profile,
    ProfilePageVisit,
)

# CUSTOM FUNCTIONS
from custom_functions.visitors_ip_address import get_ip
from custom_functions.visitors_user_agent import get_user_agent
from custom_functions.social_media_button_click_processor import social_media_button_click_processor
from custom_functions.document_click_coordinate_processor import document_click_coordinate_processor
from custom_functions.mouse_trace_processor import mouse_trace_processor
from custom_functions.keystroke_processor import keystroke_processor

# FORMS
from .forms import (
    UserRegisterForm,
    UserUpdateForm,
    ProfileUpdateForm,
)



# Configuring debugging feature code
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Disabling the debugging feature. Hint: Comment out this line to enable debugging.
# disable(CRITICAL)



# VIEW FUNCTIONS



##############################

# REGISTER PAGE

##############################

def register(request):
    """A view function rendering the register page."""

    ip = get_ip(request)
    user_agent = get_user_agent(request)

    if request.POST.get("id") == "register_page_visit_information":

        RegisterPageVisit.objects.create(ip_address=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"))

    social_media_button_click_processor(request=request, id="smbci", ip=ip, user_agent=user_agent, platform_choice=request.POST.get("choice"), page_url=request.POST.get("current_url"))
    document_click_coordinate_processor(request=request, id="document_click_coordinate_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))
    mouse_trace_processor(request=request, id="mouse_trace_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))
    keystroke_processor(request=request, id="keystroke_request", ip=ip, user_agent=user_agent, keystroke=request.POST.get("key_value"), page_url=request.POST.get("current_url"))

    all_meta_description_objs = RegisterPageMetaDescription.objects.all()

    if request.method == 'POST':

        register_form = UserRegisterForm(request.POST)

        if register_form.is_valid():

            new_user = register_form.save()
            new_user.save()
            messages.success(request, f'Your account has been created! You are now able to login.')
            return redirect('login')

        else:
            
            debug(register_form.errors)
    
    else:
    
        register_form = UserRegisterForm()
        

    context = {
        'register_form_errors': register_form.errors,
        'all_meta_description_objs': all_meta_description_objs,
        'register_form': register_form,  
    }

    return render(request, 'accountportal/register.html', context=context)



##############################

# PROFILE PAGE

##############################

@login_required
def profile(request):

    ip = get_ip(request)
    user_agent = get_user_agent(request)

    if request.POST.get("id") == "profile_page_visit_information":

        ProfilePageVisit.objects.create(username=request.user.username, ip_address=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"))

    social_media_button_click_processor(request=request, id="smbci", ip=ip, user_agent=user_agent, platform_choice=request.POST.get("choice"), page_url=request.POST.get("current_url"))
    document_click_coordinate_processor(request=request, id="document_click_coordinate_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))
    mouse_trace_processor(request=request, id="mouse_trace_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))
    keystroke_processor(request=request, id="keystroke_request", ip=ip, user_agent=user_agent, keystroke=request.POST.get("key_value"), page_url=request.POST.get("current_url"))

    if request.method == 'POST' and "updatebtn" in request.POST:
    
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():

            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

        else:

            messages.error(request, f'{u_form.errors}')
            messages.error(request, f'{p_form.errors}')
            debug(u_form.errors)
    
    
    context = {}

    return render(request, 'accountportal/profile.html', context=context)
