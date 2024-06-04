# LIBRARIES
from django.db import models
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse
from embed_video.fields import EmbedVideoField
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Importing the validators.
from django.core.validators import FileExtensionValidator
from custom_validators.validators import validate_file_size

# MODELS
from pages.models import GlobalSubscription


# DATA CLASSES


##############################

# BLOG PAGE

##############################

class BlogPageMetaDescription(models.Model):
    
    text = models.TextField(max_length=1500, null=False, blank=False, help_text="Meta description is a HTML element that describes the page's content. Creating a meta description element is beneficial for better SEO and that's why, you should use sentences which will catch the user's attention.", default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",)

    class Meta:
    
        verbose_name_plural = "Blog Page Meta Description"

class BlogPageBlogPost(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, verbose_name="ID", help_text="Universal Unique Identifier")
    title = models.CharField(max_length=255, null=False, blank=False, default="Lorem Ipsum", unique=True, help_text="Write a title for your post.<br><strong>Note: </strong><li>Keep it concise and informative</li><li>Write for your audience</li><li>Entice the reader</li><li>Incorporate important keywords</li><li>Write in sentence case</li>")# max max_length = required

    post_types = (
        ('e', 'Exclusive'),
        ('r', 'Regular'),
    )

    post_type = models.CharField(
        max_length=1,
        choices=post_types,
        blank=False,
        null=False,
        default='r',
        help_text='<strong>Notes: </strong><li>Select a post type.</li><li>Regular posts will be send to both users and subscribers.</li><li>Exclusive posts will be send to users only.</li>', 
        verbose_name="Post Type",)

    def upload_post_image(self, field_attname):
        """A function which generates dynamic paths for post images."""
        
        return f'blog/{self.title}/{self.image}'
    
    image = models.ImageField(null=True, blank=True, upload_to=upload_post_image, help_text="<strong>Note: </strong><li>There is no specific required dimension.</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li><li>Make sure the file size is not over 30MB.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    
    def upload_post_video(self, field_attname):
        """A function which generates dynamic paths for post videos."""
        
        return f'blog/{self.title}/{self.image}'

    video = models.FileField(null=True, blank=True, upload_to=upload_post_video, help_text="Upload image or video. This application can't display both. (Prefferred image)")
    youtube_url = EmbedVideoField(max_length=1000, null=True, blank=True, help_text="<strong>Note: </strong><li>Open the video from YouTube. Press to the share > embed. Only copy paste the url that's 'src' attributes value.</li><li><strong>Ex: </strong>'https://www.youtube.com/embed/el1t1FoWdZI'</li><li><strong>Hint: Without quotes.</li>")
    date = models.DateField(auto_now_add=False, null=True, blank=True, help_text="Please use the fallowing format: YYYY-MM-DD")
    para1 = models.TextField(verbose_name="Paragraph 1", default="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", max_length=10000, null=False, blank=False, help_text="<strong>Notes: </strong><li>Unity: Ensure that your paragraph has a central idea or theme. Every sentence should contribute to or support this main point.</li><li>Topic Sentence: Begin the paragraph with a clear and concise topic sentence that introduces the main idea.</li><li>Coherence: Use logical transitions between sentences to maintain a smooth flow of ideas. This helps readers follow your thoughts easily.</li><li>Supporting Details: Provide specific examples, evidence, or details to support your main idea. This adds depth and credibility to your paragraph.</li><li>Conciseness: Be concise and avoid unnecessary words. Each sentence should contribute meaningfully to the paragraph.</li><li>Variety in Sentence Structure: Use a mix of sentence structures – short and long sentences – to add rhythm and keep the reader engaged.</li><li>Clarity: Aim for clarity in your writing. Choose words carefully, and ensure that your sentences are easy to understand.</li><li>Focus: Stick to the main point of the paragraph. Avoid introducing unrelated ideas that might confuse the reader.</li><li>Transitions: Use transitional words or phrases to guide the reader from one idea to the next. This creates a cohesive and organized paragraph.</li><li>Conclusion: End the paragraph with a concluding sentence that summarizes the main point or provides a bridge to the next paragraph.</li>")
    para2 = models.TextField(verbose_name="Paragraph 2", max_length=10000, null=True, blank=True,)
    para3 = models.TextField(verbose_name="Paragraph 3", max_length=10000, null=True, blank=True,)
    para4 = models.TextField(verbose_name="Paragraph 4", max_length=10000, null=True, blank=True,)
    para5 = models.TextField(verbose_name="Paragraph 5", max_length=10000, null=True, blank=True,)
    para6 = models.TextField(verbose_name="Paragraph 6", max_length=10000, null=True, blank=True,)
    para7 = models.TextField(verbose_name="Paragraph 7", max_length=10000, null=True, blank=True,)
    alt = models.TextField(max_length=500, null=True, blank=True, default="Blog Post", verbose_name="ALT", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).",)
    
    def __str__(self):
        """A function which returns a string which will represent the object. Hint: Now, when you crated an object these object will be named with the object's title instead of Object (1) or (2)"""
        
        return self.title
    
    def get_absolute_url(self):
        """A function which returns the url to access a particular book instance."""

        return reverse('post-detail', args=[str(self.id)])

    def send_emails(self):
        """A function sending emails to subscribers."""

        subject = f'New Blog Post: {self.title}'
        message = f'Check out my latest blog post: {self.get_absolute_url()}'
        from_email = 'dogaegeozden.online.portfolio@gmail.com'
        html_message = render_to_string('blog/post_email.html', {'post': self})
        subscriber_emails = list(set(GlobalSubscription.objects.values_list('email', flat=True)))

        if self.post_type == "r":

            send_mail(
                subject,
                message,
                from_email,
                subscriber_emails,
                fail_silently=False,
                html_message=html_message,
            )

    class Meta:

        verbose_name_plural = "Blog Page Posts"
        ordering = ['-date']

class BlogPageComment(models.Model):

    post = models.ForeignKey('BlogPageBlogPost', null=True, blank=True, related_name="comments", on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=150, null=False, blank=False,)
    text = models.TextField(max_length=1500, null=True, blank=True,)
    comment_time = models.DateTimeField(blank=True, null=True, verbose_name="Comment Time", default=timezone.now)
    ip_address = models.GenericIPAddressField(null=True, blank=True, default='N/A', verbose_name="Ip Address")
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    
    def __str__(self):
        """A function which returns a string which will represent the object. Hint: Now, when you crated an object these object will be named with the object's title instead of Object (1) or (2)"""
        
        return '%s - %s - %s' % (self.commenter_name, self.post.title, self.comment_time)

    class Meta:
        
        verbose_name_plural = "Blog Page Comments"
        ordering = ['-comment_time']

class BlogPageVisit(models.Model):

    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now)
    screen_width = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Width")
    screen_height = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Height") 

    class Meta:
        
        verbose_name_plural = 'Blog Page Visit Information'
        ordering = ['-visit_time']

class BlogPagePostDetailPageVisit(models.Model):
    
    uuid = models.CharField(max_length=500, null=False, blank=False, verbose_name="Universal Unique Identifier",)
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now)
    screen_width = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Width")
    screen_height = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Height") 

    class Meta:
        
        verbose_name_plural = 'Blog Page Post Detail Page Visit Information'
        ordering = ['-visit_time']

class BlogPagePostLike(models.Model):

    post = models.ForeignKey('BlogPageBlogPost', null=True, blank=True, related_name="likes", on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    like_time = models.DateTimeField(blank=True, null=True, verbose_name="Like Time", default=timezone.now)

    like_status_options = (
        ('l', 'Liked'),
        ('n', 'Not Liked'),
    )
    
    like_status = models.CharField(max_length=1, choices=like_status_options, blank=False, default='n', verbose_name="Like Status")

    class Meta:
        
        verbose_name_plural = 'Blog Page Like Information'
        ordering = ['-like_time']

class BlogPageShareClick(models.Model):

    uuid = models.CharField(max_length=500, null=False, blank=False, verbose_name="Universal Unique Identifier",)
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    click_time = models.DateTimeField(blank=True, null=True, verbose_name="Click Time", default=timezone.now)
    platform_choice = models.CharField(max_length=200, null=True, blank=True, verbose_name="Visitor's Platform Choice To Share The Post")
    
    class Meta:
        
        verbose_name_plural = 'Blog Page Share Button Click Data'
        ordering = ['-click_time']