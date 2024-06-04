# LIBRARIES
from django.urls import path

# VIEW FUNCTIONS
from .views import (
    home, 
    portfolio,
    certifications,
    resumes,
    contact,
    unsubscribe,
    unsubscribe_success,
)

# URL PATTERS
urlpatterns = [
    path('', home, name="home"),
    path('portfolio/', portfolio, name="portfolio"),
    path('certifications/', certifications, name="certifications"),
    path('resumes/', resumes, name="resumes"),
    path('contact/', contact, name="contact"),
    path('unsubscribe/success/', unsubscribe_success, name='unsubscribe_success'), # Note: Order of url patterns matter. If you put this path below unsubscribe, application will fail to display the unsubscription success page.
    path('unsubscribe/<str:token>/', unsubscribe, name='unsubscribe'),
]