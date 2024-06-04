# LIBRARIES
from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.template.loader import render_to_string
from uuid import uuid4

# Importing the validators.
from django.core.validators import FileExtensionValidator
from custom_validators.validators import validate_file_size



# DATA CLASSES



##############################

# GLOBAL MODELS

##############################

class GlobalBrandIdentity(models.Model):

    icon = models.FileField(null=False, blank=False, verbose_name="Portfolio Icon", default="assets/portfolio_logo.ico", upload_to='global/portfolio_icons', help_text="<strong>Note: </strong><li>It needs to be .ico file</li><li>You can use GIMP to convert png/jpg/jpeg and the like files to .ico files</li><li>Make sure the file size is below 30MB.</li>", validators=[FileExtensionValidator(['ico']), validate_file_size],)
    logo = models.ImageField(null=False, blank=False, verbose_name="Portfolio Logo", default="assets/default.jpg", upload_to="global/portfolio_icons", help_text="<strong>Note:</strong><li>Don't forget to scale down your image to improve web page performance.</li><li>Accepted file types are png, jpg and, jpeg</li><li>You can use GIMP to convert file types</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    copy_right_text = models.TextField(null=False, blank=False, verbose_name="Copy Right Text", max_length=1500, default="Copyright © 2024 Doga Ozden Creative Studio. All Rights Reserved.", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).",)
    slogan = models.CharField(null=False, blank=False, verbose_name="Slogan", max_length=200, default="Lorem Ipsum",)
    alt = models.TextField(null=False, blank=False, verbose_name="Alternative Text for The Logo", max_length=500, default="Lorem Ipsum", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).",)

    class Meta:

        verbose_name_plural = "Global Brand Identity"

class GlobalSocialMediaLinks(models.Model):

    linkedin = models.URLField(max_length=1000, null=True, blank=True, verbose_name="LinkedIn",)
    instagram = models.URLField(max_length=1000, null=True, blank=True, verbose_name="Instagram",)
    facebook = models.URLField(max_length=1000, null=True, blank=True, verbose_name="Facebook",)
    github = models.URLField(max_length=1000, null=True, blank=True, verbose_name="GitHub",)
    online_store = models.URLField(max_length=1000, null=True, blank=True, verbose_name="Online Store",)
    x = models.URLField(max_length=1000, null=True, blank=True, verbose_name="X",)
    tiktok = models.URLField(max_length=1000, null=True, blank=True, verbose_name="TikTok",)
    youtube = models.URLField(max_length=1000, null=True, blank=True, verbose_name="YouTube",)
    slideshare = models.URLField(max_length=1000, null=True, blank=True, verbose_name="Slide Share",)
    
    class Meta:

        verbose_name_plural = "Global Social Media Links"

class GlobalContactInformation(models.Model):

    email = models.CharField(max_length=1000, null=True, blank=True, verbose_name="E-Mail",)
    freelancer = models.URLField(max_length=1000, null=True, blank=True, verbose_name="Freelancer",)
    upwork = models.URLField(max_length=1000, null=True, blank=True, verbose_name="Upwork",)
    fiverr = models.URLField(max_length=1000, null=True, blank=True, verbose_name="Fiverr",)
    phone_number = models.CharField(max_length=100, null=True, blank=True, verbose_name="Phone Number",)
    address = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Address",)

    class Meta:

        verbose_name_plural = "Global Contact Information"

class GlobalSocialMediaButtonClick(models.Model):

    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    platform_choice = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Visitor's Platform Choice",)
    click_time = models.DateTimeField(blank=True, null=True, verbose_name="Click Time", default=timezone.now,)
    page_url = models.URLField(max_length=3000, null=True, blank=True, verbose_name="URL",)

    class Meta:
        
        verbose_name_plural = 'Global Social Media Button Clicks'
        ordering = ['-click_time']

class GlobalDocumentClickCoordinate(models.Model):
    
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    click_time = models.DateTimeField(blank=True, null=True, verbose_name="Click Time", default=timezone.now,)
    screen_width = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Width",)
    screen_height = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Height",)
    x_coordinate = models.PositiveIntegerField(null=True, blank=True, verbose_name="X Coordinate",)
    y_coordinate = models.PositiveIntegerField(null=True, blank=True, verbose_name="Y Coordinate",)
    page_url = models.URLField(max_length=3000, null=True, blank=True, verbose_name="URL",)
    
    class Meta:
        
        verbose_name_plural = 'Global Document Click Coordinate'
        ordering = ['-click_time']

class GlobalMouseTrace(models.Model):
    
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    movement_time = models.DateTimeField(blank=True, null=True, verbose_name="Movement Time", default=timezone.now,)
    screen_width = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Width",)
    screen_height = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Height",)
    x_coordinate = models.PositiveIntegerField(null=True, blank=True, verbose_name="X Coordinate",)
    y_coordinate = models.PositiveIntegerField(null=True, blank=True, verbose_name="Y Coordinate",)
    page_url = models.URLField(max_length=3000, null=True, blank=True, verbose_name="URL",)

    class Meta:
        
        verbose_name_plural = 'Global Mouse Trace'
        ordering = ['-movement_time']

class GlobalKeystroke(models.Model):

    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    pressing_time = models.DateTimeField(blank=True, null=True, verbose_name="Click Time", default=timezone.now,)
    keystroke = models.CharField(max_length=10, null=True, blank=True, verbose_name="Keystroke", default="N/A",)
    page_url = models.URLField(max_length=3000, null=True, blank=True, verbose_name="URL",)

    class Meta:

        verbose_name_plural = 'Global Keystroke'
        ordering = ['-pressing_time']

class GlobalMouseTrace(models.Model):
    
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    movement_time = models.DateTimeField(blank=True, null=True, verbose_name="Movement Time", default=timezone.now,)
    screen_width = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Width",)
    screen_height = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Height",)
    x_coordinate = models.PositiveIntegerField(null=True, blank=True, verbose_name="X Coordinate",)
    y_coordinate = models.PositiveIntegerField(null=True, blank=True, verbose_name="Y Coordinate",)
    page_url = models.URLField(max_length=3000, null=True, blank=True, verbose_name="URL",)

    class Meta:
        
        verbose_name_plural = 'Global Mouse Trace'
        ordering = ['-movement_time']

class GlobalSubscription(models.Model):
    
    email = models.EmailField(max_length=150, verbose_name="email",)
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=1000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    subscribing_time = models.DateTimeField(blank=True, null=True, verbose_name="Subscribe Time", default=timezone.now)

    class Meta:

        verbose_name_plural = "Global Subscriptions"
        ordering = ['-subscribing_time']
    
    def __str__(self):
        """A function returning object names."""
    
        return self.email

    def create_unsubscribe_link(self, subscription):
        """A function creating unbsubscription links for subscriptions."""

        token = uuid4()
        GlobalUnsubscribeLink.objects.create(subscription=subscription, token=token)

    def get_unsubscribe_link(self):
        """A function returning unsubscription links."""

        unsubscribe_link = GlobalUnsubscribeLink.objects.get(subscription=self)
        return f"https://dogaegeozden.com/unsubscribe/{unsubscribe_link.token}"
        # return f"http://127.0.0.1:2000/unsubscribe/{unsubscribe_link.token}"

class GlobalUnsubscribeLink(models.Model):

    subscription = models.OneToOneField(GlobalSubscription, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)



##############################

# HOME PAGE

##############################

class HomePageMetaDescription(models.Model):
    
    text = models.TextField(max_length=1500, null=False, blank=False, default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", help_text="Meta description is a HTML element that describes the page's content. Creating a meta description element is beneficial for better SEO and that's why, you should use sentences which will catch the user's attention.",)
    
    class Meta:

        verbose_name_plural = "Home Page Meta Description"

class HomePageProfilePic(models.Model):
    
    image = models.ImageField(null=False, blank=False, default="assets/default.jpg", upload_to='home/profile_pictures', help_text="<strong>Note: </strong><li>Dimension requirement is 1.3 height/width</li><li>Don't forget to scale down your images to increase load speed.</li><li>Accepted file types are png, jpg and, jpeg</li><li>You can use GIMP to change the file type/extension</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size])
    alt = models.TextField(max_length=500, null=False, blank=False, default="Lorem Ipsum", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).", verbose_name="ALT")
    
    class Meta:

        verbose_name_plural = "Home Page Profile Picture"

class HomePageBio(models.Model):
    
    text = models.TextField(max_length=10000, blank=False, null=False, default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", help_text="<strong>Notes: </strong><li>Introduce your self.</li><li>Include the most relevant professional experience.</li><li>Mention significant personal achievements or awards.</li><li>Introduce personal details.</li><li>Use a casual and friendly tone.</li>")
    
    class Meta:

        verbose_name_plural = "Home Page Bio"

class HomePageToolsOrLanguagesMainContent(models.Model):
    
    title = models.CharField(max_length=300, null=False, blank=False, default="TOOLS AND LANGUAGES", help_text="Create a title for the tools and languages section.")
    image = models.ImageField(null=False, blank=False, default="assets/default.jpg", upload_to='home/tools_and_languages_main_visuals', help_text="<strong>Note: </strong><li>Required dimension ratio = 1.2 height/width</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change the file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    alt = models.TextField(max_length=500, null=False, blank=False, default="Lorem Ipsum", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).", verbose_name="ALT")
    
    class Meta:
        
        verbose_name_plural = "Home Page Tools And Languages Section Main Content"
    
    def __str__(self):
        """A function that names the object with it's title"""
        
        return self.title

class HomePageToolOrLanguage(models.Model):
    
    title = models.CharField(max_length=300, null=False, blank=False, default="Lorem Ipsum", help_text="Create a title for the tool or language object.")
    icon_url = models.URLField(max_length=1000, null=True, blank=True, verbose_name="URL", help_text="Copy paste the url which leads to the tool's or language's icon.")
    icon_file = models.FileField(null=True, blank=True, upload_to="home/tool_or_language_icons", help_text="<strong>Note: </strong><li>Accepted file type is svg.</li><li>Make sure the file size is not over 30MB.</li>", validators=[FileExtensionValidator(['svg']), validate_file_size],)
    alt = models.TextField(max_length=500, null=False, blank=False, default="lorem ipsum", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).", verbose_name="ALT")
    
    class Meta:
        
        verbose_name_plural = "Home Page Tool or Language"
    
    def __str__(self):
        """A function that names the object with it's title"""
        
        return self.title

class HomePageToolOrLanguageImageClick(models.Model):
    
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    tool_or_language_choice = models.CharField(max_length=300, null=True, blank=True, verbose_name="Visitor's Choice")
    click_time = models.DateTimeField(blank=True, null=True, verbose_name="Click Time", default=timezone.now)
    
    class Meta:
        
        verbose_name_plural = 'Home Page Tool Or Language Image Clicks'
        ordering = ['-click_time']

class HomePageActivity(models.Model):
    
    title = models.CharField(max_length=300, null=False, blank=False, default="Lorem Ipsum", help_text="Give a title to the activiy.<br>Note: You can use the activity's name.<br>Ex: Calisthenics")
    description = models.TextField(max_length=10000, null=True, blank=True, default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",)
    
    def upload_activity_img(self, field_attname):
        """A function which creates a path to upload images."""
        
        return f'home/activities/{self.title}/{self.image}'
    
    image = models.ImageField(null=False, blank=False, default="assets/default.jpg", upload_to=upload_activity_img, help_text="<strong>Note: </strong><li>Required Dimension Ratio = 1.2 height/width</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    alt = models.TextField(max_length=500, null=False, blank=False, default="Lorem Ipsum", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).", verbose_name="ALT")
    
    class Meta:

        verbose_name_plural = "Home Page Activity"
    
    def __str__(self):
        """A function returning object name using it's title."""
        
        return self.title

class HomePageVisit(models.Model):
    
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)    
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now)
    screen_width = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Width")
    screen_height = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Height") 

    class Meta:

        verbose_name_plural = 'Home Page Visit Information'
        ordering = ['-visit_time']

class HomePageProfilePictureClick(models.Model):
    
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    profile_picture_choice = models.CharField(max_length=300, null=True, blank=True, verbose_name="Profile Picture Choice")
    click_time = models.DateTimeField(blank=True, null=True, verbose_name="Click Time", default=timezone.now)

    class Meta:
        
        verbose_name_plural = 'Home Page Profile Picture Clicks'        
        ordering = ['-click_time']

class HomePageToolsAndLanguagesImageClick(models.Model):
    
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    tools_and_languages_image_choice = models.CharField(max_length=300, null=True, blank=True, verbose_name="Visitor's Tools And Languages Image Choice")    
    click_time = models.DateTimeField(blank=True, null=True, verbose_name="Click Time", default=timezone.now)

    class Meta:
        
        verbose_name_plural = 'Home Page Tools And Languages Image Clicks'        
        ordering = ['-click_time']

class HomePageActivityImageClick(models.Model):
    
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    activity_image_choice = models.CharField(max_length=300, null=True, blank=True, verbose_name="Visitor's Activity Image Choice")
    click_time = models.DateTimeField(blank=True, null=True, verbose_name="Click Time", default=timezone.now)

    class Meta:
        
        verbose_name_plural = 'Home Page Activity Image Clicks'        
        ordering = ['-click_time']

class HomePagePartnersSectionTextContent(models.Model):

    title = models.CharField(max_length=300, null=False, blank=False, default="Lorem Ipsum", help_text="Write a header for partner section.")
    text = models.TextField(max_length=1500, null=False, blank=False, default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", help_text="Write a paragraph or sentence for partners section.",)
    
    class Meta:

        verbose_name_plural = "Home Page Partners Section Text Content"

class HomePagePartner(models.Model):

    logo = models.ImageField(verbose_name="Image", null=False, blank=False, default="assets/default.jpg", upload_to="home/partner_logos", help_text="<strong>Notes: </strong><li>Resize the logo to 200px x 200px.</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    logo_alt = models.TextField(verbose_name="Alternative Text for The Partner's Logo", max_length=1000, null=False, blank=False, default="Lorem Ipsum", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).",)

    class Meta:

        verbose_name_plural = "Home Page Partner"



##############################

# PORTFOLIO PAGE

##############################

class PortfolioPageMetaDescription(models.Model):
    
    text = models.TextField(max_length=1500, null=False, blank=False, default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", help_text="Meta description is a HTML element that describes the page's content. Creating a meta description element is beneficial for better SEO and that's why, you should use sentences which will catch the user's attention.",)
    
    class Meta:
        
        verbose_name_plural = "Portfolio Page Meta Description"

class PortfolioPagePhotoGridColumn1Image(models.Model):

    img = models.ImageField(verbose_name="Image", null=False, blank=False, default="assets/default.jpg", upload_to="portfolio/photogrid", help_text="<strong>Notes: </strong><li>There is no specific dimension requirement.</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    img_alt = models.TextField(verbose_name="Alternative Text", max_length=1000, null=False, blank=False, default="Lorem Ipsum", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).",)

    class Meta:

        verbose_name_plural = "Portfolio Page Photo Grid Column 1 Image"

class PortfolioPagePhotoGridColumn2Image(models.Model):

    img = models.ImageField(verbose_name="Image", null=False, blank=False, default="assets/default.jpg", upload_to="portfolio/photogrid", help_text="<strong>Notes: </strong><li>There is no specific dimension requirement.</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    img_alt = models.TextField(verbose_name="Alternative Text", max_length=1000, null=False, blank=False, default="Lorem Ipsum", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).",)

    class Meta:

        verbose_name_plural = "Portfolio Page Photo Grid Column 2 Image"

class PortfolioPagePhotoGridColumn3Image(models.Model):

    img = models.ImageField(verbose_name="Image", null=False, blank=False, default="assets/default.jpg", upload_to="portfolio/photogrid", help_text="<strong>Notes: </strong><li>There is no specific dimension requirement.</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    img_alt = models.TextField(verbose_name="Alternative Text", max_length=1000, null=False, blank=False, default="Lorem Ipsum", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).",)

    class Meta:

        verbose_name_plural = "Portfolio Page Photo Grid Column 3 Image"

class PortfolioPagePhotoGridColumn4Image(models.Model):

    img = models.ImageField(verbose_name="Image", null=False, blank=False, default="assets/default.jpg", upload_to="portfolio/photogrid", help_text="<strong>Notes: </strong><li>There is no specific dimension requirement.</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    img_alt = models.TextField(verbose_name="Alternative Text", max_length=1000, null=False, blank=False, default="Lorem Ipsum", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).",)

    class Meta:

        verbose_name_plural = "Portfolio Page Photo Grid Column 4 Image"

class PortfolioPageSlideShowVideo(models.Model):

    video = models.FileField(verbose_name="Video", null=False, blank=False, upload_to="portfolio/videoslideshow", help_text="<strong>Notes: </strong><li>All videos has to be in mp4 format</li><li>You can convert videos to mp4 format using Blender.</li><li>File size should not exceed 30MB.</li>",  validators=[FileExtensionValidator(['mp4']), validate_file_size])
    video_alt = models.TextField(verbose_name="Alternative Text", max_length=1000, null=False, blank=False, default="Lorem Ipsum", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).",)

    class Meta:

        verbose_name_plural = "Portfolio Page Slide Show Video"

class PortfolioPageWebDevelopment(models.Model):
   
    title = models.CharField(max_length=255, unique=True, null=False, blank=False, default="Lorem Ipsum", help_text="Write the name of the project.")
    web_page_link = models.URLField(max_length=750, null=False, blank=False, default="https://webpage.com/", help_text="<li>Copy paste the project page's link</li>", verbose_name="Web Page Link")

    def upload_web_page_image(self, field_attname):
        """A function which generates dynamic paths for web pages' preview images"""
        
        return f'web_pages/{self.title}/{self.preview_image}'

    preview_image = models.ImageField(verbose_name="Preview Image", null=False, blank=False, default="assets/default.jpg", upload_to=upload_web_page_image, help_text="<strong>Notes: </strong><li>There is no specific dimension requirement.</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    preview_image_alt = models.TextField(verbose_name="Alternative Text for The Preview Image", max_length=1000, null=False, blank=False, default="Lorem Ipsum", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).",)

    class Meta:

        verbose_name_plural = "Portfolio Page Web Development"

    def __str__(self):
        """A function returning strings for object names using their titles."""

        return self.title

class PortfolioPageVisit(models.Model):
    
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now)
    screen_width = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Width")
    screen_height = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Height") 
    
    class Meta:

        verbose_name_plural = 'Portfolio Page Visit Information'
        ordering = ['-visit_time']

class PortfolioPageGraphicDesignProjClickData(models.Model):

    project_choice = models.CharField(max_length=300, null=True, blank=True, verbose_name="Visitor's Project Choice")
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    click_time = models.DateTimeField(blank=True, null=True, verbose_name="Click Time", default=timezone.now)
    
    class Meta:

        verbose_name_plural = "Portfolio Page Graphic Design Project Click Data"
        ordering = ["-click_time"]

class PortfolioPageWebDevProjClickData(models.Model):

    project_choice = models.CharField(max_length=300, null=True, blank=True, verbose_name="Visitor's Project Choice")
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    click_time = models.DateTimeField(blank=True, null=True, verbose_name="Click Time", default=timezone.now)
    
    class Meta:

        verbose_name_plural = "Portfolio Page Web Development Project Link Click Data"
        ordering = ["-click_time"]



##############################

# CERTIFICATIONS PAGE

##############################

class CertificationsPageMetaDescription(models.Model):
    
    text = models.TextField(max_length=1500, null=False, blank=False, default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", help_text="Meta description is a HTML element that describes the page's content. Creating a meta description element is beneficial for better SEO and that's why, you should use sentences which will catch the user's attention.")
    
    class Meta:

        verbose_name_plural = "Certifications Page Meta Description"


class CertificationsPageCertification(models.Model):
    
    title = models.CharField(max_length=255, unique=True, null=False, blank=False, default="Lorem Ipsum", help_text="Write the title of your certification.<br><strong>Hint: </strong>You can simply write the name of the certification.")
    topic = models.CharField(max_length=300, null=False, blank=False, default="Lorem Ipsum", help_text="Write a topic which categorizes your application.<br><strong>Ex: </strong>Microsoft Office")
    
    def upload_certification(self, field_attname):
        """A function which generates dynamic paths for certifications"""
        
        return f'certifications/{self.topic}/{self.digital_copy}'
    
    digital_copy = models.FileField(verbose_name="Digital Copy", null=True, blank=True, upload_to=upload_certification, help_text="<strong>Note: </strong><li>There is no specific required dimension.</li><li>Accepted file types are pdf, png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li><li>Make sure the file size is not over 30MB.</li>", validators=[FileExtensionValidator(['pdf', 'png', 'jpg', 'jpeg']), validate_file_size],)
    digital_copy_url = models.URLField(verbose_name="URL of The Certification", null=True, blank=True, help_text="Add a URL leading to your certification if you don't have a digital copy.", max_length=255)
    issuer = models.CharField(max_length=300, null=False, blank=False, default="Lorem Ipsum", help_text="Write the name of the organization who issued this certification.")
    issue_date = models.DateField(auto_now_add=False, null=True, blank=True, verbose_name="Issue Date", help_text="Please use the fallowing format: YYYY-MM-DD")
    expiry_date = models.DateField(auto_now_add=False, null=True, blank=True, verbose_name="Expiry Date", help_text="Please use the fallowing format: YYYY-MM-DD")

    class Meta:

        verbose_name_plural = "Certifications Page Certification"
   
    def __str__(self):
        """String for representing the model object."""
        
        return self.title

class CertificationsPageVisit(models.Model):
    
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now)
    screen_width = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Width")
    screen_height = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Height") 
    
    class Meta:
        
        verbose_name_plural = 'Certification Page Visit Information'
        ordering = ['-visit_time']

class CertificationsPageCertificationClick(models.Model):
    
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    certification_choice = models.CharField(max_length=300, null=True, blank=True, verbose_name="Visitor's Certification Choice")
    click_time = models.DateTimeField(blank=True, null=True, verbose_name="Click Time", default=timezone.now)
    
    class Meta:
        
        verbose_name_plural = 'Certifications Page Certification Clicks'
        ordering = ['-click_time']



##############################

# RESUMES PAGE

##############################

class ResumesPageMetaDescription(models.Model):

    text = models.TextField(max_length=1500, null=False, blank=False, default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", help_text="Meta description is a HTML element that describes the page's content. Creating a meta description element is beneficial for better SEO and that's why, you should use sentences which will catch the user's attention.")

    class Meta:

        verbose_name_plural = "Resumes Page Meta Description"

class ResumesPageAboutCurrentPosition(models.Model):

    text = models.TextField(max_length=3000, null=False, blank=False, default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", help_text="Explain what are dealing with currently as the third person.<br><strong>Ex: </strong>A self taught programmer seeking for a full time position, where he can utilize his skills and knowledge in web development field.")

    class Meta:

        verbose_name_plural = "Resumes Page About Current Position"

class ResumesPageResume(models.Model):

    field_name = models.CharField(max_length=300, null=False, blank=False, verbose_name="Field Name", default="Lorem Ipsum", help_text="Write the name of the field which you prepared resume for.")
    resume_name = models.CharField(max_length=300, null=False, blank=False, verbose_name="Resume Name", default="Lorem Ipsum", help_text="Give your resume a name.<br><strong>Note: </strong>This name will be used to name the object.")
    
    def upload_resume_file(self, field_attname):
        """A function which generates dynamic paths for resume files."""

        return f'resumes/{self.field_name}/{self.file}'

    file = models.FileField(null=False, blank=False, default="/assets/resume_dogaegeozden_full_stack_web_developer.pdf", upload_to=upload_resume_file, help_text="<strong>Note: </strong><li>There is no specific required dimension.</li><li>Accepted file type is pdf.</li><li>You can use the Libre Writer to convert word files to pdf files.</li><li>Make sure the file size is not over 30MB.</li>", validators=[FileExtensionValidator(['pdf']), validate_file_size],)

    class Meta:

        verbose_name_plural = "Resumes Page Resume"

    def __str__(self):
        """String for representing the model object."""

        return self.resume_name

class ResumesPageExperience(models.Model):

    job_title = models.CharField(max_length=300, null=False, blank=False, verbose_name="Job Title", default="Lorem Ipsum", help_text="Write the job title of your experience.")# max max_length = required
    company_name = models.CharField(max_length=300, null=False, blank=False, verbose_name="Company Name", default="Lorem Ipsum", help_text="Write the name of the company that you worked for.")# max max_length = required
    
    work_Status = (
        ('p', 'Present'),
        ('c', 'Complete'),
    )
    
    start_date = models.DateField(auto_now_add=False, null=True, blank=True, verbose_name="Start Date", help_text="Please use the fallowing format: YYYY-MM-DD")
    end_date = models.DateField(auto_now_add=False, null=True, blank=True, verbose_name="End Date", help_text="Please use the fallowing format: YYYY-MM-DD")
    
    working_status = models.CharField(
        max_length=1,
        choices=work_Status,
        blank=False,
        null=False,
        default='n',
        help_text='Working status', 
        verbose_name="Working Status",)
    
    text = models.TextField(max_length=550, blank=True, null=True, help_text="Write a short job description.")
    header = models.CharField(max_length=200, null=True, blank=True, help_text="Write a header which will be located on top of the list item. Ex: Summary")
    list_item_1 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="List Item 1", help_text="Write a task that you completed during your experience.")
    list_item_2 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="List Item 2", help_text="Write a task that you completed during your experience.")
    list_item_3 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="List Item 3", help_text="Write a task that you completed during your experience.")
    list_item_4 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="List Item 4", help_text="Write a task that you completed during your experience.")
    list_item_5 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="List Item 5", help_text="Write a task that you completed during your experience.")
    
    def upload_experience_image_1(self, field_attname):
        """A function which generates dynamic paths for experience images."""

        return f'experience/{self.company_name}/{self.img_1}'

    img_1 = models.ImageField(null=True, blank=True, upload_to=upload_experience_image_1, verbose_name="Experince Picture 1", help_text="<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    
    def upload_experience_image_2(self, field_attname):
        """A function which generates dynamic paths for experience images."""

        return f'experience/{self.company_name}/{self.img_2}'

    img_2 = models.ImageField(null=True, blank=True, upload_to=upload_experience_image_2, verbose_name="Experince Picture 2", help_text="<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)

    def upload_experience_image_3(self, field_attname):
        """A function which generates dynamic paths for experience images."""

        return f'experience/{self.company_name}/{self.img_3}'
 
    img_3 = models.ImageField(null=True, blank=True, upload_to=upload_experience_image_3, verbose_name="Experince Picture 3", help_text="<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)

    def upload_experience_image_4(self, field_attname):
        """A function which generates dynamic paths for experience images."""
        
        return f'experience/{self.company_name}/{self.img_4}'

    img_4 = models.ImageField(null=True, blank=True, upload_to=upload_experience_image_4, verbose_name="Experince Picture 4", help_text="<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)

    def upload_experience_image_5(self, field_attname):
        """A function which generates dynamic paths for experience images."""
        
        return f'experience/{self.company_name}/{self.img_5}'

    img_5 = models.ImageField(null=True, blank=True, upload_to=upload_experience_image_5, verbose_name="Experince Picture 5", help_text="<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)

    def upload_experience_image_6(self, field_attname):
        """A function which generates dynamic paths for experience images."""

        return f'experience/{self.company_name}/{self.img_6}'

    img_6 = models.ImageField(null=True, blank=True, upload_to=upload_experience_image_6, verbose_name="Experince Picture 6", help_text="<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)

    def upload_experience_image_7(self, field_attname):
        """A function which generates dynamic paths for experience images."""

        return f'experience/{self.company_name}/{self.img_7}'

    img_7 = models.ImageField(null=True, blank=True, upload_to=upload_experience_image_7, verbose_name="Experince Picture 7", help_text="<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)

    def upload_experience_image_8(self, field_attname):
        """A function which generates dynamic paths for experience images."""

        return f'experience/{self.company_name}/{self.img_8}'

    img_8 = models.ImageField(null=True, blank=True, upload_to=upload_experience_image_8, verbose_name="Experince Picture 8", help_text="<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)

    def upload_experience_image_9(self, field_attname):
        """A function which generates dynamic paths for experience images."""

        return f'experience/{self.company_name}/{self.img_9}'

    img_9 = models.ImageField(null=True, blank=True, upload_to=upload_experience_image_9, verbose_name="Experince Picture 9", help_text="<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)

    def upload_experience_image_10(self, field_attname):
        """A function which generates dynamic paths for experience images."""

        return f'experience/{self.company_name}/{self.img_10}'

    img_10 = models.ImageField(null=True, blank=True, upload_to=upload_experience_image_10, verbose_name="Experince Picture 10", help_text="<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
   
    class Meta:

        verbose_name_plural = "Resumes Page Experience"
   
    def __str__(self):
        """String for representing the model object."""

        return self.job_title

class ResumesPageEducation(models.Model):

    name = models.CharField(max_length=250, null=False, blank=False, verbose_name="School Name", help_text="Write the name of the college/university that you have graduated from.")
    city = models.CharField(max_length=200, null=True, blank=True, help_text="Write the name of the city where your college/university is located.")
    province = models.CharField(max_length=200, null=True, blank=True, help_text="Write the name of the province where your college/university is located.")
    start_date = models.DateField(auto_now_add=False, null=True, blank=True, verbose_name="Start Date", help_text="Please use the fallowing format: YYYY-MM-DD")
    end_date = models.DateField(auto_now_add=False, null=True, blank=True, verbose_name="End Date", help_text="Please use the fallowing format: YYYY-MM-DD")
    major = models.CharField(max_length=300, null=False, blank=False, verbose_name="Major", default="Lorem Ipsum", help_text="Write your program's name.")
    diploma = models.TextField(max_length=300, null=True, blank=True, verbose_name="Diploma", default="Lorem Ipsum", help_text="Write the name of the diploma that you received.")
    para = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Paragraph", help_text="Write a short paragraph that best describes your college/university.")
    alt = models.TextField(max_length=3000, null=False, blank=False, verbose_name="ALT", default="Lorem Ipsum", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).",)

    class Meta:

        verbose_name_plural = "Resumes Page Education"
    
    def __str__(self):
        """String for representing the model object."""

        return self.name

class ResumesPageVisit(models.Model):

    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now)
    screen_width = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Width")
    screen_height = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Height")
   
    class Meta:

        verbose_name_plural = 'Resume Page Visit Information'
        ordering = ['-visit_time']

class ResumesPageResumeFileClicks(models.Model):

    resume_choice = models.CharField(max_length=500, null=True, blank=True, verbose_name="Visitor's Resume Choice")
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    click_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now)
    
    class Meta:

        verbose_name_plural = 'Resumes Page Resume File Click Information'
        ordering = ['-click_time']



##############################

# CONTACT PAGE

##############################

class ContactPageMetaDescription(models.Model):

    text = models.TextField(max_length=1500, null=False, blank=False, default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

    class Meta:

        verbose_name_plural = "Contact Page Meta Description"

class ContactPageContactPPic(models.Model):

    image = models.ImageField(null=False, blank=False, default="assets/default.jpg", upload_to="contact_page_pictures", help_text="<strong>Note: </strong><li>Required dimension ratio = 1.2 height/width</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li><li>Make sure the file size is not over 30MB.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    alt = models.TextField(max_length=500, null=False, blank=False, default="Lorem Ipsum", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).", verbose_name="ALT")
    
    class Meta:

        verbose_name_plural = "Contact Page Picture"

class ContactPageMessage(models.Model):

    first_name = models.CharField(max_length=250, verbose_name="First Name")
    last_name = models.CharField(max_length=250, default='N/A', verbose_name="Last Name")
    email = models.EmailField(max_length=350, verbose_name="E-mail")
    phone_number = models.CharField(max_length=100, default='N/A', verbose_name="Phone Number")
    message = models.TextField(max_length=7500, verbose_name="Message")
    message_sending_time = models.DateTimeField(blank=True, null=True, verbose_name="Submit Time", default=timezone.now)
    ip_address = models.GenericIPAddressField(null=True, blank=True, default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)

    def send_emails(self):

        subject = f'New Contact Message: {self.first_name} {self.last_name}'
        message = f'{self.message}'
        from_email = 'dogaegeozden.online.portfolio@gmail.com'
        to_email = ['dogaegeozden@gmail.com',]
        html_message = render_to_string('contact/contact_message_email.html', {'contact_message': self})

        send_mail(
            subject,
            message,
            from_email,
            to_email,
            fail_silently=False,
            html_message=html_message,
        )

    class Meta:

        verbose_name_plural = "Contact Page Messages"

class ContactPageVisit(models.Model):

    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now,)
    screen_width = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Width",)
    screen_height = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Height",)

    class Meta:

        verbose_name_plural = 'Contact Page Visit Information'
        ordering = ['-visit_time']



##############################

# UNSUBSCRIBE PAGE

##############################

class UnsubscribePageVisit(models.Model):

    token = models.CharField(max_length=255, unique=True,)
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now,)
    screen_width = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Width",)
    screen_height = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Height",) 

    class Meta:

        verbose_name_plural = 'Unsubscribe Page Visit Information'
        ordering = ['-visit_time']