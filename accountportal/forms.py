# LIBRARIES
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_recaptcha.fields import ReCaptchaField

# MODELS
from django.contrib.auth.models import User
from .models import Profile


# FORM CLASSES

class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField()
    captcha = ReCaptchaField()

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    
    email = forms.EmailField()

    class Meta:

        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        
        model = Profile

        fields = [
            
            'full_name',
            'image',
        
        ]

    full_name = forms.CharField(max_length=250, label="Full Name")