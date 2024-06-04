# LIBRARIES
from django.db import models
from django.utils import timezone



# DATA CLASSES



##############################

# PRIVACY POLICY PAGE

##############################

# Creating a data class called PrivacyPolicyPageMetaDescription to control how the objects will be created/stored in the database.
class PrivacyPolicyPageMetaDescription(models.Model):
    
    text = models.TextField(max_length=1500, null=False, blank=False, default="Your privacy is important to me.",)

    class Meta:
        
        verbose_name_plural = "Privacy Policy Page Meta Description"

# Creating a data class called PrivacyPolicyPageVisit to control how the objects will be created/stored in the database.
class PrivacyPolicyPageVisit(models.Model):
    
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now)
    screen_width = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Width")
    screen_height = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Height")

    class Meta:
        
        verbose_name_plural = 'Privacy Policy Page Visit Information'     
        ordering = ['-visit_time']
        
class PrivacyPolicy(models.Model):

    effective_date = models.DateField(auto_now_add=False, null=True, blank=True, verbose_name="Effective Date", help_text="Please use the fallowing format: YYYY-MM-DD")
    section_1_title = models.CharField(max_length=500, null=True, blank=True, help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.")
    section_1_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Write section's content and make sure you are using a proper language", verbose_name="Section Text")
    section_2_title = models.CharField(max_length=500, null=True, blank=True, help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.")
    section_2_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Write section's content and make sure you are using a proper language", verbose_name="Section Text")
    section_3_title = models.CharField(max_length=500, null=True, blank=True, help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.")
    section_3_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Write section's content and make sure you are using a proper language", verbose_name="Section Text")
    section_4_title = models.CharField(max_length=500, null=True, blank=True, help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.")
    section_4_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Write section's content and make sure you are using a proper language", verbose_name="Section Text")
    section_5_title = models.CharField(max_length=500, null=True, blank=True, help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.")
    section_5_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Write section's content and make sure you are using a proper language", verbose_name="Section Text")
    section_6_title = models.CharField(max_length=500, null=True, blank=True, help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.")
    section_6_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Write section's content and make sure you are using a proper language", verbose_name="Section Text")
    section_7_title = models.CharField(max_length=500, null=True, blank=True, help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.")
    section_7_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Write section's content and make sure you are using a proper language", verbose_name="Section Text")
    section_8_title = models.CharField(max_length=500, null=True, blank=True, help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.")
    section_8_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Write section's content and make sure you are using a proper language", verbose_name="Section Text")
    section_9_title = models.CharField(max_length=500, null=True, blank=True, help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.")
    section_9_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Write section's content and make sure you are using a proper language", verbose_name="Section Text")
    section_10_title = models.CharField(max_length=500, null=True, blank=True, help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.")
    section_10_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Write section's content and make sure you are using a proper language", verbose_name="Section Text")
    section_11_title = models.CharField(max_length=500, null=True, blank=True, help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.")
    section_11_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Write section's content and make sure you are using a proper language", verbose_name="Section Text")
    section_12_title = models.CharField(max_length=500, null=True, blank=True, help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.")
    section_12_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Write section's content and make sure you are using a proper language", verbose_name="Section Text")
    references_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Let people know if you used anysoftware to create this privacy policy", verbose_name="Citation Text")

    class Meta:
        
        verbose_name_plural = 'Privacy Policy'



##############################

# TERMS AND CONDITIONS PAGE

##############################

class TermsAndConditionsPageMetaDescription(models.Model):
    
    text = models.TextField(max_length=1500, null=False, blank=False, default="Your privacy is important to me.",)
    
    class Meta:
    
        verbose_name_plural = "Terms And Conditions Page Meta Description"

class TermsAndConditionsPageVisit(models.Model):

    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=6000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now)
    screen_width = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Width")
    screen_height = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Height")

    class Meta:
        
        verbose_name_plural = 'Terms And Conditions Page Visit Information'
        ordering = ['-visit_time']

class TermsAndConditions(models.Model):

    effective_date = models.DateField(auto_now_add=False, null=True, blank=True, verbose_name="Effective Date", help_text="Please use the fallowing format: YYYY-MM-DD")
    section_1_title = models.CharField(max_length=500, null=True, blank=True, help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.")
    section_1_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Write section's content and make sure you are using a proper language", verbose_name="Section Text")
    section_2_title = models.CharField(max_length=500, null=True, blank=True, help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.")
    section_2_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Write section's content and make sure you are using a proper language", verbose_name="Section Text")
    section_3_title = models.CharField(max_length=500, null=True, blank=True, help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.")
    section_3_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Write section's content and make sure you are using a proper language", verbose_name="Section Text")
    section_4_title = models.CharField(max_length=500, null=True, blank=True, help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.")
    section_4_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Write section's content and make sure you are using a proper language", verbose_name="Section Text")
    section_5_title = models.CharField(max_length=500, null=True, blank=True, help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.")
    section_5_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Write section's content and make sure you are using a proper language", verbose_name="Section Text")
    section_6_title = models.CharField(max_length=500, null=True, blank=True, help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.")
    section_6_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Write section's content and make sure you are using a proper language", verbose_name="Section Text")
    section_7_title = models.CharField(max_length=500, null=True, blank=True, help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.")
    section_7_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Write section's content and make sure you are using a proper language", verbose_name="Section Text")
    section_8_title = models.CharField(max_length=500, null=True, blank=True, help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.")
    section_8_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Write section's content and make sure you are using a proper language", verbose_name="Section Text")
    section_9_title = models.CharField(max_length=500, null=True, blank=True, help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.")
    section_9_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Write section's content and make sure you are using a proper language", verbose_name="Section Text")
    section_10_title = models.CharField(max_length=500, null=True, blank=True, help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.")
    section_10_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Write section's content and make sure you are using a proper language", verbose_name="Section Text")
    section_11_title = models.CharField(max_length=500, null=True, blank=True, help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.")
    section_11_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Write section's content and make sure you are using a proper language", verbose_name="Section Text")
    section_12_title = models.CharField(max_length=500, null=True, blank=True, help_text="<strong>Notes: </strong><li>Make sure only first letter of each word is capital.")
    section_12_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Write section's content and make sure you are using a proper language", verbose_name="Section Text")
    references_text = models.TextField(max_length=6000, null=True, blank=True, help_text="Let people know if you used anysoftware to create this terms and conditions", verbose_name="Citation Text")

    class Meta:

        verbose_name_plural = 'Terms And Conditions'