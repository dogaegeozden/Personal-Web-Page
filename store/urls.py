# LIBRARIES
from django.urls import path

# VIEW FUNCTIONS
from .views import (
    services,
    service_detail,
    books,
    book_detail,
)

# URL PATTERS
urlpatterns = [
    path('services/', services, name="services"),
    path('services/<slug:slug>', service_detail, name="service-detail"),
    path('books/', books, name="books"),
    path('books/<uuid:id>', book_detail, name="book-detail"),
]