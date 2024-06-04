# LIBRARIES AND MODULES
from django.db.models.signals import post_save
from django.dispatch import receiver

# MODELS
from .models import (
    GlobalSubscription,
    
    ContactPageMessage,
)

@receiver(post_save, sender=ContactPageMessage)
def send_email_on_new_contact_message(sender, instance, created, **kwargs):

    if created:
    
        # Send email logic here
        instance.send_emails()  # Assuming you have a method in your model for sending emails

@receiver(post_save, sender=GlobalSubscription)
def create_unsubscribe_link_signal(sender, instance, created, **kwargs):

    if created:

        instance.create_unsubscribe_link(instance)