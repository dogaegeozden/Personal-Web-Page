# MODULES/LIBRARIES
from django.contrib import messages

# MODELS
from .models import (
    GlobalBrandIdentity,
    GlobalSocialMediaLinks,
    GlobalContactInformation,
    GlobalSubscription,
)

# CUSTOM FUNCTIONS
from custom_functions.visitors_ip_address import get_ip
from custom_functions.visitors_user_agent import get_user_agent

# FORMS
from .forms import SubscriptionForm



# CONTEXT PROCESSORS



def social_media_link_processor(request):
    """A context processor function that makes all social media links accessible in the entire web page"""

    all_social_media_link_objs = GlobalSocialMediaLinks.objects.all()

    return {'all_social_media_link_objs': all_social_media_link_objs}


def contact_information_processor(request):
    """A context processor function that makes all social media links accessible in the entire web page"""

    all_contact_information_objs = GlobalContactInformation.objects.all()

    return {'all_contact_information_objs': all_contact_information_objs}


def cookie_notice_processor(request):
    """A context processor function that makes the variables required for the cookie notice function, accessible in the entire web application"""

    cookie_notice_answer = request.session.get('cookie_notice_answer', 0)

    if request.method == "POST" and 'iGotIt' in request.POST:

        if cookie_notice_answer <= 1:

            cookie_notice_answer = request.session.get('cookie_notice_answer', 1)
            request.session['cookie_notice_answer'] = cookie_notice_answer + 1

        elif cookie_notice_answer >= 2:

            request.session['cookie_notice_answer'] = cookie_notice_answer

    context = {
        
        'cookie_notice_answer': cookie_notice_answer,

    }

    return context


def brand_identity_processor(request):
    """A context processor function which makes portfolio icon accessible in all pages"""
    
    all_brand_identity_objs = GlobalBrandIdentity.objects.all()

    return {'all_brand_identity_objs': all_brand_identity_objs}


def subscription_form_processor(request):
    """A context processor function which makes the subscription form available all over the web application."""
        
    ip = get_ip(request)
    user_agent = get_user_agent(request)
    
    subscription_form = SubscriptionForm()
    
    if request.method == 'POST' and 'subscribeBtn' in request.POST:
    
        subscription_form = SubscriptionForm(request.POST)
    
        if subscription_form.is_valid():
    
            GlobalSubscription.objects.create(ip_address=ip, user_agent=user_agent, **subscription_form.cleaned_data)
            subscription_form = SubscriptionForm()
            messages.success(request, f'Thank You!')
    
        else:
    
            print(subscription_form.errors)
        
    context = {

        'sForm': subscription_form,

    }
    
    return context