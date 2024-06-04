# LIBRARIES
from django.shortcuts import render
from logging import basicConfig, DEBUG, debug, disable, CRITICAL

# MODELS
from .models import (
    PrivacyPolicyPageMetaDescription,
    PrivacyPolicyPageVisit,
    PrivacyPolicy,

    TermsAndConditionsPageMetaDescription,
    TermsAndConditionsPageVisit,
    TermsAndConditions,
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



# VIEW FUNCTIONS



##############################

# PRIVACY POLICY PAGE

##############################

def privacy_policy(request):
    """A view function which renders the privacy policy page."""

    ip = get_ip(request)
    user_agent = get_user_agent(request)

    if request.POST.get("id") == "privacy_policy_page_visit_information":

        PrivacyPolicyPageVisit.objects.create(ip_address=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"))

    social_media_button_click_processor(request=request, id="smbci", ip=ip, user_agent=user_agent, platform_choice=request.POST.get("choice"), page_url=request.POST.get("current_url"))
    document_click_coordinate_processor(request=request, id="document_click_coordinate_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))
    mouse_trace_processor(request=request, id="mouse_trace_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))
    keystroke_processor(request=request, id="keystroke_request", ip=ip, user_agent=user_agent, keystroke=request.POST.get("key_value"), page_url=request.POST.get("current_url"))

    all_meta_description_objs = PrivacyPolicyPageMetaDescription.objects.all()
    all_privacy_policy_objs = PrivacyPolicy.objects.all()

    context = {

        'all_meta_description_objs': all_meta_description_objs,
        'all_privacy_policy_objs': all_privacy_policy_objs

    }

    return render(request, 'privacy_policy/privacy_policy.html', context=context)



##############################

# TERMS AND CONDITIONS PAGE

##############################

def terms_and_conditions(request):
    """A view function for the terms and conditions page of the online portfolio application"""

    ip = get_ip(request)
    user_agent = get_user_agent(request)

    if request.POST.get("id") == "terms_and_conditions_page_visit_information":

        TermsAndConditionsPageVisit.objects.create(ip_address=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"))

    social_media_button_click_processor(request=request, id="smbci", ip=ip, user_agent=user_agent, platform_choice=request.POST.get("choice"), page_url=request.POST.get("current_url"))
    document_click_coordinate_processor(request=request, id="document_click_coordinate_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))
    mouse_trace_processor(request=request, id="mouse_trace_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))
    keystroke_processor(request=request, id="keystroke_request", ip=ip, user_agent=user_agent, keystroke=request.POST.get("key_value"), page_url=request.POST.get("current_url"))

    all_meta_description_objs = TermsAndConditionsPageMetaDescription.objects.all()
    all_terms_and_conditions_objs = TermsAndConditions.objects.all()

    context = {

        'all_meta_description_objs': all_meta_description_objs,
        'all_terms_and_conditions_objs': all_terms_and_conditions_objs,

    }

    return render(request, 'terms_and_conditions/terms_and_conditions.html', context)
