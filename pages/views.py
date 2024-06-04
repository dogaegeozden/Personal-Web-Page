# LIBRARIES
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect
from logging import basicConfig, DEBUG, debug, disable, CRITICAL

# FORMS
from .forms import SubscriptionForm, MessageForm

# MODELS
from .models import (
    GlobalUnsubscribeLink,

    HomePageMetaDescription,
    HomePageProfilePic,
    HomePageBio, 
    HomePageToolsOrLanguagesMainContent, 
    HomePageToolOrLanguage,
    HomePageToolOrLanguageImageClick,
    HomePageActivity, 
    HomePageVisit, 
    HomePageProfilePictureClick, 
    HomePageToolsAndLanguagesImageClick,
    HomePageActivityImageClick,
    HomePagePartnersSectionTextContent,
    HomePagePartner,

    PortfolioPageMetaDescription,
    PortfolioPagePhotoGridColumn1Image,
    PortfolioPagePhotoGridColumn2Image,
    PortfolioPagePhotoGridColumn3Image,
    PortfolioPagePhotoGridColumn4Image,
    PortfolioPageSlideShowVideo, 
    PortfolioPageWebDevelopment, 
    PortfolioPageVisit, 
    PortfolioPageGraphicDesignProjClickData, 
    PortfolioPageWebDevProjClickData,

    CertificationsPageMetaDescription,
    CertificationsPageCertification,
    CertificationsPageVisit,
    CertificationsPageCertificationClick,

    ResumesPageMetaDescription,
    ResumesPageAboutCurrentPosition,
    ResumesPageResume,
    ResumesPageExperience,
    ResumesPageEducation,
    ResumesPageVisit,
    ResumesPageResumeFileClicks,

    ContactPageMetaDescription,
    ContactPageContactPPic,
    ContactPageMessage,
    ContactPageVisit,

    UnsubscribePageVisit,
)

# CUSTOM FUNCTIONS
from custom_functions.visitors_ip_address import get_ip
from custom_functions.visitors_user_agent import get_user_agent
from custom_functions.social_media_button_click_processor import social_media_button_click_processor
from custom_functions.document_click_coordinate_processor import document_click_coordinate_processor
from custom_functions.mouse_trace_processor import mouse_trace_processor
from custom_functions.keystroke_processor import keystroke_processor


# Doing the basic configuration for the debugging feature
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Disabling the debugging feature. Hint: Comment out this line to enable debugging.
# disable(CRITICAL)



# VIEW FUNCTIONS



##############################

# HOME PAGE

##############################

def home(request):
    """A view function to render the main page of the online portfolio"""

    ip = get_ip(request)

    user_agent = get_user_agent(request)    

    if request.POST.get("id") == "main_page_visit_information":

        HomePageVisit.objects.create(ip_address=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"))

    social_media_button_click_processor(request=request, id="smbci", ip=ip, user_agent=user_agent, platform_choice=request.POST.get("choice"), page_url=request.POST.get("current_url"))

    document_click_coordinate_processor(request=request, id="document_click_coordinate_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))

    mouse_trace_processor(request=request, id="mouse_trace_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))

    keystroke_processor(request=request, id="keystroke_request", ip=ip, user_agent=user_agent, keystroke=request.POST.get("key_value"), page_url=request.POST.get("current_url"))

    all_meta_description_objs = HomePageMetaDescription.objects.all()

    all_profile_picture_objs = HomePageProfilePic.objects.all()

    all_bio_objs = HomePageBio.objects.all()

    all_tools_and_languages_main_visual_objs = HomePageToolsOrLanguagesMainContent.objects.all()

    all_tools_and_languages_objs = HomePageToolOrLanguage.objects.all()

    all_activity_objs = HomePageActivity.objects.all()

    all_clients_section_text_content_objs = HomePagePartnersSectionTextContent.objects.all()

    all_client_objs = HomePagePartner.objects.all()

    if request.POST.get("id") == "profile_picture_choice_request":

        HomePageProfilePictureClick.objects.create(ip_address=ip, user_agent=user_agent, profile_picture_choice=request.POST.get("choice"),)

    if request.POST.get("id") == "activity_image_choice_request":

        HomePageActivityImageClick.objects.create(ip_address=ip, user_agent=user_agent, activity_image_choice=request.POST.get("choice"),)

    if request.POST.get("id") == "tools_and_languages_image_click_data_request":

        HomePageToolsAndLanguagesImageClick.objects.create(tools_and_languages_image_choice=request.POST.get("choice"), ip_address=ip, user_agent=user_agent)
    
    if request.POST.get("id") == "tool_or_language_choice_request":

        HomePageToolOrLanguageImageClick.objects.create(ip_address=ip, user_agent=user_agent, tool_or_language_choice=request.POST.get("choice"))

    context = {

        'all_meta_description_objs': all_meta_description_objs,

        'all_profile_picture_objs': all_profile_picture_objs,

        'all_bio_objs': all_bio_objs,

        'all_tools_and_languages_main_visual_objs': all_tools_and_languages_main_visual_objs,

        'all_tools_and_languages_objs': all_tools_and_languages_objs,

        'all_activity_objs': all_activity_objs,

        'all_clients_section_text_content_objs': all_clients_section_text_content_objs,

        'all_client_objs': all_client_objs,

    }

    return render(request, 'home/home.html', context=context)



##############################

# PORTFOLIO PAGE

##############################

def portfolio(request):
    """A view function for the portfolio page of the online portfolio application"""

    ip = get_ip(request)

    user_agent = get_user_agent(request)

    if request.POST.get("id") == "portfolio_page_visit_information":

        PortfolioPageVisit.objects.create(ip_address=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"))

    social_media_button_click_processor(request=request, id="smbci", ip=ip, user_agent=user_agent, platform_choice=request.POST.get("choice"), page_url=request.POST.get("current_url"))

    document_click_coordinate_processor(request=request, id="document_click_coordinate_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))

    mouse_trace_processor(request=request, id="mouse_trace_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))

    keystroke_processor(request=request, id="keystroke_request", ip=ip, user_agent=user_agent, keystroke=request.POST.get("key_value"), page_url=request.POST.get("current_url"))

    all_meta_description_objs = PortfolioPageMetaDescription.objects.all()

    all_photo_grid_column1_objs = PortfolioPagePhotoGridColumn1Image.objects.all()

    all_photo_grid_column2_objs = PortfolioPagePhotoGridColumn2Image.objects.all()

    all_photo_grid_column3_objs = PortfolioPagePhotoGridColumn3Image.objects.all()

    all_photo_grid_column4_objs = PortfolioPagePhotoGridColumn4Image.objects.all()

    all_video_slide_show_objs = PortfolioPageSlideShowVideo.objects.all()

    all_web_development_objs = PortfolioPageWebDevelopment.objects.all()

    if request.POST.get("id") == "graphic_design_project_click_data":
        
        PortfolioPageGraphicDesignProjClickData.objects.create(project_choice=request.POST.get("choice"), ip_address=ip, user_agent=user_agent)

    if request.POST.get("id") == "web_development_project_link_click_data":

        PortfolioPageWebDevProjClickData.objects.create(project_choice=request.POST.get("choice"), ip_address=ip, user_agent=user_agent)

    context = {

        
        'all_meta_description_objs': all_meta_description_objs,
        
        'all_photo_grid_column1_objs': all_photo_grid_column1_objs,
        
        'all_photo_grid_column2_objs': all_photo_grid_column2_objs,
        
        'all_photo_grid_column3_objs': all_photo_grid_column3_objs,
        
        'all_photo_grid_column4_objs': all_photo_grid_column4_objs,
        
        'all_video_slide_show_objs': all_video_slide_show_objs,
        
        'all_web_development_objs': all_web_development_objs,

    }

    return render(request, 'portfolio/portfolio.html', context=context)



##############################

# CERTIFICATIONS PAGE

##############################

def certifications(request):
    """A view function which renders the certifications page."""

    ip = get_ip(request)

    user_agent = get_user_agent(request)

    if request.POST.get("id") == "certifications_page_visit_information":

        CertificationsPageVisit.objects.create(ip_address=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"))

    social_media_button_click_processor(request=request, id="smbci", ip=ip, user_agent=user_agent, platform_choice=request.POST.get("choice"), page_url=request.POST.get("current_url"))

    document_click_coordinate_processor(request=request, id="document_click_coordinate_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))

    mouse_trace_processor(request=request, id="mouse_trace_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))

    keystroke_processor(request=request, id="keystroke_request", ip=ip, user_agent=user_agent, keystroke=request.POST.get("key_value"), page_url=request.POST.get("current_url"))

    all_meta_description_objs = CertificationsPageMetaDescription.objects.all()

    all_certification_objs = CertificationsPageCertification.objects.all()

    if request.POST.get("id") == "certchoinf": 

        CertificationsPageCertificationClick.objects.create(ip_address=ip, user_agent=user_agent, certification_choice=request.POST.get("choice"))

    context = {

        'all_meta_description_objs': all_meta_description_objs,
        
        'all_certification_objs': all_certification_objs,
    
    }

    return render(request, 'certifications/certifications.html', context=context)



##############################

# RESUMES PAGE

##############################

def resumes(request):
    """A view function for the resumes page of the online portfolio application"""

    ip = get_ip(request)

    user_agent = get_user_agent(request)

    if request.POST.get("id") == "resumes_page_visit_information":

        ResumesPageVisit.objects.create(ip_address=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"))

    social_media_button_click_processor(request=request, id="smbci", ip=ip, user_agent=user_agent, platform_choice=request.POST.get("choice"), page_url=request.POST.get("current_url"))

    document_click_coordinate_processor(request=request, id="document_click_coordinate_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))

    mouse_trace_processor(request=request, id="mouse_trace_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))

    keystroke_processor(request=request, id="keystroke_request", ip=ip, user_agent=user_agent, keystroke=request.POST.get("key_value"), page_url=request.POST.get("current_url"))

    all_meta_description = ResumesPageMetaDescription.objects.all()

    all_about_current_position_objs = ResumesPageAboutCurrentPosition.objects.all()

    # Creating a query set from all the objects that are created in the database with the ResumesPageExperince data model.
    all_experience_objs = ResumesPageExperience.objects.all()

    # Creating a query set from all the objects that are created in the database with the ResumesPageEducation data model.
    all_education_objs = ResumesPageEducation.objects.all()

    # Creating a query set from all the objects that are created in the database with the ResumesPageResume data model.
    all_resume_objs = ResumesPageResume.objects.all()

    # Checking if the post request's id is equal to resume_choice_request
    if request.POST.get("id") == "resume_choice_request":

        # Creating an object in the database using the ResumeFileClicks data model.
        ResumesPageResumeFileClicks.objects.create(resume_choice=request.POST.get("resumeChoice"), ip_address=ip, user_agent=user_agent)

    # Creating a dictionary called context from the key value pairs.
    context = {

        'all_meta_description': all_meta_description,
        
        'all_about_current_position_objs': all_about_current_position_objs,
        
        'all_experience_objs': all_experience_objs,
        
        'all_education_objs': all_education_objs,
        
        'all_resume_objs': all_resume_objs,
    
    }

    # Rendering the request, html page and the context dictionary.
    return render(request, 'resumes/resumes.html', context=context)



##############################

# CONTACT PAGE

##############################

def contact(request):
    """A view function to render contact page of the online portfolio application"""

    ip = get_ip(request)

    user_agent = get_user_agent(request)

    if request.POST.get("id") == "contact_page_visit_information":

        ContactPageVisit.objects.create(ip_address=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"))

    social_media_button_click_processor(request=request, id="smbci", ip=ip, user_agent=user_agent, platform_choice=request.POST.get("choice"), page_url=request.POST.get("current_url"))

    document_click_coordinate_processor(request=request, id="document_click_coordinate_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))

    mouse_trace_processor(request=request, id="mouse_trace_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))

    keystroke_processor(request=request, id="keystroke_request", ip=ip, user_agent=user_agent, keystroke=request.POST.get("key_value"), page_url=request.POST.get("current_url"))

    all_contact_page_picture_obj = ContactPageContactPPic.objects.all()

    all_meta_description_objs = ContactPageMetaDescription.objects.all()

    contact_form = MessageForm()

    if request.method == "POST" and 'msgSendBtn' in request.POST:

        contact_form = MessageForm(request.POST)

        if contact_form.is_valid():

            ContactPageMessage.objects.create(ip_address=ip, user_agent=user_agent, first_name=contact_form.cleaned_data['first_name'], last_name=contact_form.cleaned_data['last_name'], email=contact_form.cleaned_data['email'], phone_number=contact_form.cleaned_data['phone_number'], message=contact_form.cleaned_data['message'])

            messages.success(request, 'Your message has been delivered!')

            contact_form = MessageForm()

            return HttpResponseRedirect("/contact/")

        else:

            messages.error(request, 'We could not process your request at the moment. Please try again later.')

            debug(contact_form.errors)

    context = {

        "all_meta_description_objs": all_meta_description_objs,
        
        "all_contact_page_picture_obj": all_contact_page_picture_obj,

        "contact_form": contact_form,
    
    }

    return render(request, 'contact/contact.html', context=context)



##############################

# UNSUBSCRIBE PAGE

##############################

def unsubscribe(request, token):
    """A view function which renders the unsubscribe pages."""

    ip = get_ip(request)

    user_agent = get_user_agent(request)

    unsubscribe_link = get_object_or_404(GlobalUnsubscribeLink, token=token)

    subscription = unsubscribe_link.subscription

    if request.POST.get("id") == "unsubscribe_page_visit_information":

        UnsubscribePageVisit.objects.create(token=token, ip_address=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"))

    social_media_button_click_processor(request=request, id="smbci", ip=ip, user_agent=user_agent, platform_choice=request.POST.get("choice"), page_url=request.POST.get("current_url"))

    document_click_coordinate_processor(request=request, id="document_click_coordinate_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))

    mouse_trace_processor(request=request, id="mouse_trace_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))

    keystroke_processor(request=request, id="keystroke_request", ip=ip, user_agent=user_agent, keystroke=request.POST.get("key_value"), page_url=request.POST.get("current_url"))

    if request.method == 'POST' and "UnsubscribeBtn" in request.POST:

        subscription.delete()

        return redirect('unsubscribe_success')

    return render(request, 'unsubscribe/unsubscribe.html', {'subscription': subscription})


def unsubscribe_success(request):

    return render(request, 'unsubscribe/unsubscribe_success.html')