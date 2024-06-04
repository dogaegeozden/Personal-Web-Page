# LIBRARIES
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BlogPageBlogPost

@receiver(post_save, sender=BlogPageBlogPost)
def send_email_on_new_post(sender, instance, created, **kwargs):

    if created:

        # Send email logic here
        instance.send_emails()  # Assuming you have a method in your model for sending emails
