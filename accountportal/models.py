# LIBRARIES
from django.db import models
from django.utils import timezone
from PIL import Image

# Importing the validators.
from django.core.validators import FileExtensionValidator
from custom_validators.validators import validate_file_size

# MODELS
from django.contrib.auth.models import User



# DATA CLASSES


##############################

# LOGIN PAGE

##############################

class LoginPageMetaDescription(models.Model):
    
    text = models.TextField(max_length=1500, null=False, blank=False, default="Securely access your personalized space at Doga Ege Ozden's online portfolio. Login now to explore exclusive content, projects, and updates. Streamlined authentication for a seamless experience. Your gateway to a world of creativity and innovation.", help_text="Meta description is a HTML element that describes the page's content. Creating a meta description element is beneficial for better SEO and that's why, you should use sentences which will catch the user's attention.",)
    
    class Meta:

        verbose_name_plural = "Login Page Meta Description"


##############################

# LOGOUT PAGE

##############################

class LogoutPageMetaDescription(models.Model):
    
    text = models.TextField(max_length=1500, null=False, blank=False, default="Logout securely from Doga Ege Ozden's online portfolio. Safely end your session and protect your account. Login to explore exclusive content, projects, and updates. Streamlined authentication for a seamless experience. Your gateway to a world of creativity and innovation.", help_text="Meta description is a HTML element that describes the page's content. Creating a meta description element is beneficial for better SEO and that's why, you should use sentences which will catch the user's attention.",)
    
    class Meta:

        verbose_name_plural = "Logout Page Meta Description"


##############################

# REGISTER PAGE

##############################

# Creating a data class called RegisterPageDescription to control how objects will be created/stored in the database.
class RegisterPageMetaDescription(models.Model):
    
    text = models.TextField(max_length=1500, null=False, blank=False, default="Join my vibrant community and immerse yourself in a world of thought-provoking blogs and exclusive content. Register for free today and gain access to a treasure trove of knowledge and inspiration. Elevate your understanding and stay at the forefront of your field. Sign up now and embark on a journey of intellectual enrichment!", help_text="Meta description is a HTML element that describes the page's content. Creating a meta description element is beneficial for better SEO and that's why, you should use sentences which will catch the user's attention.",)
    
    class Meta:

        verbose_name_plural = "Register Page Meta Description"

# Creating a class called RegisterPageVisit to control how the objects will be created/stored in the database.
class RegisterPageVisit(models.Model):

    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now)
    screen_width = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Width")
    screen_height = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Height") 
    
    class Meta:

        verbose_name_plural = 'Register Page Visit Information'
        ordering = ['-visit_time']


##############################

# PROFILE PAGE

##############################

# Creating a class called ProfilePageVisit to control how the objects will be created/stored in the database.
class ProfilePageVisit(models.Model):

    username = models.CharField(max_length=150, null=True, blank=True, verbose_name="Username", )
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now)
    screen_width = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Width")
    screen_height = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Height") 
    
    class Meta:

        verbose_name_plural = 'Profile Page Visit Information'
        ordering = ['-visit_time']

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def upload_profile_picture(self, field_attname):
        """A function creating dyanmic upload paths for profile pictures."""

        return f'profiles/{self.user.username}/{self.image}'

    full_name = models.CharField(verbose_name="Full Name", max_length=250, null=True, blank=True,)
    image = models.ImageField(default='assets/default_user_profile_picture.jpg', upload_to=upload_profile_picture, validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)

    def __str__(self):
        """A function returning object names."""

        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        """A function editing profile photos before saving."""

        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:

            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:

        verbose_name_plural = "Profile Page Profile"


##############################

# PASSWORD RESET COMPLETE PAGE

##############################

class PasswordResetCompletePageMetaDescription(models.Model):
    
    text = models.TextField(max_length=1500, null=False, blank=False, default="Successfully reset your password on Doga Ege Ozden's online portfolio. Followed our secure instructions to update your account. Log in again and continue exploring exclusive content, projects, and updates. Your gateway to a world of creativity and innovation.",)
    
    class Meta:
        
        verbose_name_plural = "Password Reset Complete Page Meta Description"


##############################

# PASSWORD RESET CONFIRM PAGE

##############################

class PasswordResetConfirmPageMetaDescription(models.Model):
    
    text = models.TextField(max_length=1500, null=False, blank=False, default="Set a new secure password for your account on Doga Ege Ozden's online portfolio. Follow the provided instructions to strengthen the security of your profile. Safely update your password and continue exploring exclusive content, projects, and updates. Your gateway to a world of creativity and innovation.",)
    
    class Meta:
        
        verbose_name_plural = "Password Reset Confirm Page Meta Description"


##############################

# PASSWORD RESET DONE PAGE

##############################

class PasswordResetDonePageMetaDescription(models.Model):
    
    text = models.TextField(max_length=1500, null=False, blank=False, default="Receive instructions for resetting your password securely. Check your email for the password reset link. If you haven't received it, please check your spam folder. Contact our support team for assistance.",)
    
    class Meta:
        
        verbose_name_plural = "Password Reset Done Page Meta Description"


##############################

# PASSWORD RESET FORM PAGE

##############################

class PasswordResetFormPageMetaDescription(models.Model):
    
    text = models.TextField(max_length=1500, null=False, blank=False, default="Reset your password securely for Doga Ege Ozden's online portfolio. Safely update your account password. Explore exclusive content, projects, and updates. Streamlined authentication for a seamless experience. Your gateway to a world of creativity and innovation.",)
    
    class Meta:
        
        verbose_name_plural = "Password Reset Form Page Meta Description"
