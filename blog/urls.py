# LIBRARIES
from django.urls import path

# VIEW FUNCTIONS
from .views import (
    blog,
    post_detail_view,
)

# URL PATTERS
urlpatterns = [
    path('blog/', blog, name="blog"),
    path('blog/<uuid:id>', post_detail_view, name="post-detail"),
]