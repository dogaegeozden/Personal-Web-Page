# LIBRARIES
from django.urls import path

# VIEW FUNCTIONS
from .views import privacy_policy, terms_and_conditions

# URL PATTERNS
urlpatterns = [
    path('privacy-policy/', privacy_policy, name="privacy-policy"),
    path('terms-and-conditions/', terms_and_conditions, name="terms-and-conditions"),
]
