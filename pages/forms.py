# LIBRARIES
from django import forms
from django_recaptcha.fields import ReCaptchaField

# MODELS
from .models import GlobalSubscription, ContactPageMessage



# FORM CLASSES



class SubscriptionForm(forms.ModelForm):
    
    class Meta:
    
        model = GlobalSubscription

        fields = [
            'email',
        ]

    email = forms.EmailField(max_length=150, label="E-mail")

class MessageForm(forms.ModelForm):

    class Meta:

        model = ContactPageMessage

        fields = [

            'first_name',
            'last_name',
            'email',
            'phone_number',
            'message',

        ]

    first_name = forms.CharField(max_length=250, label="First Name")
    last_name = forms.CharField(max_length=250, required=False, label="Last Name")
    email = forms.EmailField(max_length=350, label="E-mail")
    phone_number = forms.CharField(max_length=100, required=False, label="Phone Number")
    message = forms.CharField(max_length=7500, label="Message")
    captcha = ReCaptchaField()
