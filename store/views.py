# LIBRARIES
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from logging import basicConfig, DEBUG, debug, disable, CRITICAL

# MODELS
from .models import (
    ServicesPageMetaDescription,
    ServicesPageMainContent,
    ServicesPageService,
    ServicesPageVisit,
    ServiceDetailPageVisit,

    BooksPageMetaDescription,
    BooksPageBook,
    BooksPageVisit,
    BookDetailPageVisit,
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



##############################

# SERVICES PAGE

##############################

def services(request):
    """A view function which renders the services page."""

    ip = get_ip(request)
    user_agent = get_user_agent(request)

    if request.POST.get('id') == 'services_page_visit_information':

        ServicesPageVisit.objects.create(ip_address=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"))

    social_media_button_click_processor(request=request, id="smbci", ip=ip, user_agent=user_agent, platform_choice=request.POST.get("choice"), page_url=request.POST.get("current_url"))
    document_click_coordinate_processor(request=request, id="document_click_coordinate_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))
    mouse_trace_processor(request=request, id="mouse_trace_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))
    keystroke_processor(request=request, id="keystroke_request", ip=ip, user_agent=user_agent, keystroke=request.POST.get("key_value"), page_url=request.POST.get("current_url"))

    all_meta_description_objs = ServicesPageMetaDescription.objects.all()
    all_services_page_main_content_objs = ServicesPageMainContent.objects.all()
    all_service_objs = ServicesPageService.objects.all()

    context = {
        'all_meta_description_objs': all_meta_description_objs,
        'all_services_page_main_content_objs': all_services_page_main_content_objs,
        'all_service_objs': all_service_objs,
    }

    return render(request, 'services/services.html', context=context)


def service_detail(request, slug):
    """A view function which renders the service detail pages."""

    context = {}

    service_detail = get_object_or_404(ServicesPageService, slug=slug)

    ip = get_ip(request)
    user_agent = get_user_agent(request)

    if request.POST.get("id") == "service_detail_page_visit_information":

        ServiceDetailPageVisit.objects.create(ip_address=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"))

    social_media_button_click_processor(request=request, id="smbci", ip=ip, user_agent=user_agent, platform_choice=request.POST.get("choice"), page_url=request.POST.get("current_url"))
    document_click_coordinate_processor(request=request, id="document_click_coordinate_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))
    mouse_trace_processor(request=request, id="mouse_trace_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))
    keystroke_processor(request=request, id="keystroke_request", ip=ip, user_agent=user_agent, keystroke=request.POST.get("key_value"), page_url=request.POST.get("current_url"))

    context['service_detail'] = service_detail

    return render(request, 'services/service_detail.html', context=context)



##############################

# BOOKS PAGE

##############################

def books(request):
    """A view function which renders the books page."""

    ip = get_ip(request)
    user_agent = get_user_agent(request)

    if request.POST.get('id') == 'books_page_visit_information':

        BooksPageVisit.objects.create(ip_address=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"))

    social_media_button_click_processor(request=request, id="smbci", ip=ip, user_agent=user_agent, platform_choice=request.POST.get("choice"), page_url=request.POST.get("current_url"))
    document_click_coordinate_processor(request=request, id="document_click_coordinate_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))
    mouse_trace_processor(request=request, id="mouse_trace_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))
    keystroke_processor(request=request, id="keystroke_request", ip=ip, user_agent=user_agent, keystroke=request.POST.get("key_value"), page_url=request.POST.get("current_url"))

    all_meta_description_objs = BooksPageMetaDescription.objects.all()
    all_book_objs = BooksPageBook.objects.all()

    context = {
        'all_meta_description_objs': all_meta_description_objs,
        'all_book_objs': all_book_objs,
    }

    return render(request, 'books/books.html', context=context)


def book_detail(request, id):
    """A view function which renders the book detail pages."""

    context = {}

    book_detail = get_object_or_404(BooksPageBook, id=id)

    ip = get_ip(request)
    user_agent = get_user_agent(request)

    if request.POST.get("id") == "book_detail_page_visit_information":

        BookDetailPageVisit.objects.create(ip_address=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"))

    social_media_button_click_processor(request=request, id="smbci", ip=ip, user_agent=user_agent, platform_choice=request.POST.get("choice"), page_url=request.POST.get("current_url"))
    document_click_coordinate_processor(request=request, id="document_click_coordinate_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))
    mouse_trace_processor(request=request, id="mouse_trace_request", ip=ip, user_agent=user_agent, screen_width=request.POST.get("width"), screen_height=request.POST.get("height"), x_coordinate=request.POST.get("x_coordinate"), y_coordinate=request.POST.get("y_coordinate"), page_url=request.POST.get("current_url"))
    keystroke_processor(request=request, id="keystroke_request", ip=ip, user_agent=user_agent, keystroke=request.POST.get("key_value"), page_url=request.POST.get("current_url"))

    context['book_detail'] = book_detail

    return render(request, 'books/book_detail.html', context=context)
