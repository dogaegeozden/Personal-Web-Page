# LIBRARIES
from django.db import models
from uuid import uuid4
from django.utils import timezone
from django.urls import reverse

# Importing the validators.
from django.core.validators import FileExtensionValidator
from custom_validators.validators import validate_file_size



##############################

# SERVICES PAGE

##############################

class ServicesPageMetaDescription(models.Model):
    
    text = models.TextField(max_length=1500, null=False, blank=False, default="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", help_text="Meta description is a HTML element that describes the page's content. Creating a meta description element is beneficial for better SEO and that's why, you should use sentences which will catch the user's attention.",)

    class Meta:

        verbose_name_plural = "Services Page Meta Description"

class ServicesPageVisit(models.Model):

    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now)
    screen_width = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Width")
    screen_height = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Height")

    class Meta:

        verbose_name_plural = 'Services Page Visit Information'
        ordering = ['-visit_time']

class ServicesPageMainContent(models.Model):

    video = models.FileField(null=True, blank=True, upload_to="services", help_text="Upload image or video. This application can't display both. (Video is preferred)")
    alt = models.TextField(verbose_name="Alternative Text", max_length=500, null=False, blank=False, default="Lorem ipsum", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).",)
    para1 = models.TextField(verbose_name="Paragraph 1", default="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", max_length=10000, null=False, blank=False, help_text="<strong>How to write a paragraph?</strong><li>Unity: Ensure that your paragraph has a central idea or theme. Every sentence should contribute to or support this main point.</li><li>Topic Sentence: Begin the paragraph with a clear and concise topic sentence that introduces the main idea.</li><li>Coherence: Use logical transitions between sentences to maintain a smooth flow of ideas. This helps readers follow your thoughts easily.</li><li>Conciseness: Be concise and avoid unnecessary words. Each sentence should contribute meaningfully to the paragraph.</li><li>Variety in Sentence Structure: Use a mix of sentence structures – short and long sentences – to add rhythm and keep the reader engaged.</li><li>Clarity: Aim for clarity in your writing. Choose words carefully, and ensure that your sentences are easy to understand.</li><li>Focus: Stick to the main point of the paragraph. Avoid introducing unrelated ideas that might confuse the reader.</li><li>Transitions: Use transitional words or phrases to guide the reader from one idea to the next. This creates a cohesive and organized paragraph.</li><li>Conclusion: End the paragraph with a concluding sentence that summarizes the main point or provides a bridge to the next paragraph.</li>")
    para2 = models.TextField(verbose_name="Paragraph 2", max_length=10000, null=True, blank=True,)
    para3 = models.TextField(verbose_name="Paragraph 3", max_length=10000, null=True, blank=True,)

    class Meta:

        verbose_name_plural = "Services Page Main Content"

class ServicesPageService(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, verbose_name="ID", help_text="Universal Unique Identifier")
    slug = models.SlugField(unique=True, null=False, blank=False, help_text="Enter a sub domain for your service detail page. Ex: lorem_ipsum")
    service_title = models.CharField(verbose_name="Service Title", unique=True, max_length=255, null=False, blank=False, default="Lorem Ipsum", help_text="Write a title for the service that you are providing.")
    meta_description = models.TextField(max_length=1500, null=False, blank=False, default="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", help_text="Meta description is a HTML element that describes the page's content. Creating a meta description element is beneficial for better SEO and that's why, you should use sentences which will catch the user's attention.",)
    call_to_action_sentence = models.TextField(verbose_name="Call to Action", max_length=3000, null=False, blank=False, default="Lorem Ipsum is simply dummy text of the printing and typesetting industry.", help_text="<strong>Notes:</strong><li>Imperative Sentence (Command): Transform your professional image today – invest in a business card that speaks volumes about your brand!</li><li>Question Sentence: Ready to make a lasting impression? Invest in our exclusive business card design service today.</li><li>Offer-Based Sentence: Unlock the potential of impactful networking! Purchase our business card design service and receive a complimentary consultation.</li><li>Benefit-Focused Sentence: Stand out from the crowd and leave a lasting impression with our unique business card designs. Order yours now!</li>")

    def upload_thumbnail_picture(self, field_attname):
        """A function which generates dynamic paths for service frame pictures."""

        return f'services/{self.service_title}/{self.thumbnail_picture}'

    thumbnail_picture = models.ImageField(verbose_name="Thumbnail Picture", default="assets/default.jpg", null=False, blank=False, upload_to=upload_thumbnail_picture, help_text="<strong>Note: </strong><li>There is no specific required dimension.</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li><li>Make sure the file size is not over 30MB.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    alt_for_thumbnail_picture = models.TextField(verbose_name="Alternative Text", max_length=500, null=False, blank=False, default="Lorem ipsum", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).",)

    def upload_processs_chart(self, field_attname):
        """A function which generates dynamic paths for service's process chart."""

        return f'services/{self.service_title}/{self.process_chart}'

    process_chart = models.ImageField(verbose_name="Process Chart", default="assets/default.jpg", null=False, blank=False, upload_to=upload_processs_chart, help_text="<strong>Note: </strong><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li><li>Make sure the file size is not over 30MB.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    process_chart_alt = models.TextField(verbose_name="Alternative Text for The Process Chart", max_length=500, null=False, blank=False, default="Lorem ipsum", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).",)
    header1 = models.CharField(max_length=300, null=False, blank=False, verbose_name="Header 1", default="Lorem Ipsum", help_text="Write a title for the service that you are providing.")

    def upload_service_image1(self, field_attname):
        """A function which generates dynamic paths for service images."""

        return f'services/{self.service_title}/{self.image1}'

    image1 = models.ImageField(verbose_name="Image 1", default="assets/default.jpg", null=False, blank=False, upload_to=upload_service_image1, help_text="<strong>Note: </strong><li>There is no specific required dimension.</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li><li>Make sure the file size is not over 30MB.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    alt1 = models.TextField(verbose_name="Alternative Text 1", max_length=500, null=False, blank=False, default="Lorem ipsum", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).",)
    para1 = models.TextField(verbose_name="Paragraph 1", default="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", max_length=10000, null=False, blank=False, help_text="<strong>How to write a paragraph?</strong><li>Unity: Ensure that your paragraph has a central idea or theme. Every sentence should contribute to or support this main point.</li><li>Topic Sentence: Begin the paragraph with a clear and concise topic sentence that introduces the main idea.</li><li>Coherence: Use logical transitions between sentences to maintain a smooth flow of ideas. This helps readers follow your thoughts easily.</li><li>Conciseness: Be concise and avoid unnecessary words. Each sentence should contribute meaningfully to the paragraph.</li><li>Variety in Sentence Structure: Use a mix of sentence structures – short and long sentences – to add rhythm and keep the reader engaged.</li><li>Clarity: Aim for clarity in your writing. Choose words carefully, and ensure that your sentences are easy to understand.</li><li>Focus: Stick to the main point of the paragraph. Avoid introducing unrelated ideas that might confuse the reader.</li><li>Transitions: Use transitional words or phrases to guide the reader from one idea to the next. This creates a cohesive and organized paragraph.</li><li>Conclusion: End the paragraph with a concluding sentence that summarizes the main point or provides a bridge to the next paragraph.</li>")
    para2 = models.TextField(verbose_name="Paragraph 2", max_length=10000, null=True, blank=True,)
    para3 = models.TextField(verbose_name="Paragraph 3", max_length=10000, null=True, blank=True,)
    header2 = models.CharField(max_length=300, null=True, blank=True, verbose_name="Header 2", default="Lorem Ipsum", help_text="Write a title for the service that you are providing.")

    def upload_service_image2(self, field_attname):
        """A function which generates dynamic paths for service images."""

        return f'services/{self.service_title}/{self.image2}'

    image2 = models.ImageField(verbose_name="Image 2", null=True, blank=True, upload_to=upload_service_image2, help_text="<strong>Note: </strong><li>There is no specific required dimension.</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li><li>Make sure the file size is not over 30MB.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    alt2 = models.TextField(verbose_name="Alternative Text 2", max_length=500, null=True, blank=True, help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).",)
    para4 = models.TextField(verbose_name="Paragraph 4", max_length=10000, null=True, blank=True,)
    para5 = models.TextField(verbose_name="Paragraph 5", max_length=10000, null=True, blank=True,)
    para6 = models.TextField(verbose_name="Paragraph 6", max_length=10000, null=True, blank=True,)
    header3 = models.CharField(max_length=300, null=True, blank=True, verbose_name="Header 3", default="Lorem Ipsum", help_text="Write a title for the service that you are providing.")

    def upload_service_image3(self, field_attname):
        """A function which generates dynamic paths for service images."""

        return f'services/{self.service_title}/{self.image3}'

    image3 = models.ImageField(verbose_name="Image 3", null=True, blank=True, upload_to=upload_service_image3, help_text="<strong>Note: </strong><li>There is no specific required dimension.</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li><li>Make sure the file size is not over 30MB.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    alt3 = models.TextField(verbose_name="Alternative Text 3", max_length=500, null=True, blank=True, help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).",)
    para7 = models.TextField(verbose_name="Paragraph 7", max_length=10000, null=True, blank=True,)
    para8 = models.TextField(verbose_name="Paragraph 8", max_length=10000, null=True, blank=True,)
    para9 = models.TextField(verbose_name="Paragraph 9", max_length=10000, null=True, blank=True,)

    class Meta:

        verbose_name_plural = "Services Page Service"

    def __str__(self):
        """A function which returns a string which will represent the object."""

        return self.slug

    def get_absolute_url(self):
        """A function which returns the url to access a particular service instance."""

        return reverse('service-detail', args=[str(self.slug)])

class ServiceDetailPageVisit(models.Model):

    uuid = models.CharField(max_length=500, null=False, blank=False, verbose_name="Universal Unique Identifier",)
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now)
    screen_width = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Width")
    screen_height = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Height")
    
    class Meta:

        verbose_name_plural = 'Service Detail Page Visit Information'
        ordering = ['-visit_time']



##############################

# BOOKS PAGE

##############################

class BooksPageMetaDescription(models.Model):

    text = models.TextField(max_length=1500, null=False, blank=False, default="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", help_text="Meta description is a HTML element that describes the page's content. Creating a meta description element is beneficial for better SEO and that's why, you should use sentences which will catch the user's attention.",)

    class Meta:

        verbose_name_plural = "Books Page Meta Description"

class BooksPageBook(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, verbose_name="ID", help_text="Universal Unique Identifier")
    book_title = models.CharField(verbose_name="Book Title", unique=True, max_length=255, null=False, blank=False, default="Lorem Ipsum", help_text="Write a title for the service that you are providing.")
    author = models.CharField(verbose_name="Author's Name", max_length=300, null=False, blank=False, default="Lorem Ipsum", help_text="Write your name or name of the author.")
    meta_description = models.TextField(max_length=1500, null=False, blank=False, default="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", help_text="Meta description is a HTML element that describes the page's content. Creating a meta description element is beneficial for better SEO and that's why, you should use sentences which will catch the user's attention.",)
    short_summary = models.TextField(verbose_name="Short Summary", default="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", max_length=10000, null=False, blank=False, help_text="<strong>How to write a paragraph?</strong><li>Unity: Ensure that your paragraph has a central idea or theme. Every sentence should contribute to or support this main point.</li><li>Topic Sentence: Begin the paragraph with a clear and concise topic sentence that introduces the main idea.</li><li>Coherence: Use logical transitions between sentences to maintain a smooth flow of ideas. This helps readers follow your thoughts easily.</li><li>Conciseness: Be concise and avoid unnecessary words. Each sentence should contribute meaningfully to the paragraph.</li><li>Variety in Sentence Structure: Use a mix of sentence structures – short and long sentences – to add rhythm and keep the reader engaged.</li><li>Clarity: Aim for clarity in your writing. Choose words carefully, and ensure that your sentences are easy to understand.</li><li>Focus: Stick to the main point of the paragraph. Avoid introducing unrelated ideas that might confuse the reader.</li><li>Transitions: Use transitional words or phrases to guide the reader from one idea to the next. This creates a cohesive and organized paragraph.</li><li>Conclusion: End the paragraph with a concluding sentence that summarizes the main point or provides a bridge to the next paragraph.</li>")
    call_to_action_sentence = models.TextField(verbose_name="Call to Action", max_length=3000, null=False, blank=False, default="Lorem Ipsum is simply dummy text of the printing and typesetting industry.", help_text="<strong>Notes:</strong><li>Imperative Sentence (Command): Transform your professional image today – invest in a business card that speaks volumes about your brand!</li><li>Question Sentence: Ready to make a lasting impression? Invest in our exclusive business card design service today.</li><li>Offer-Based Sentence: Unlock the potential of impactful networking! Purchase our business card design service and receive a complimentary consultation.</li><li>Benefit-Focused Sentence: Stand out from the crowd and leave a lasting impression with our unique business card designs. Order yours now!</li>")

    def upload_thumbnail_picture(self, field_attname):
        """A function which generates dynamic paths for service frame pictures."""

        return f'books/{self.book_title}/{self.thumbnail_picture}'

    thumbnail_picture = models.ImageField(verbose_name="Thumbnail Picture", default="assets/default.jpg", null=False, blank=False, upload_to=upload_thumbnail_picture, help_text="<strong>Note: </strong><li>There is no specific required dimension.</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li><li>Make sure the file size is not over 30MB.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    thumbnail_pic_alt = models.TextField(verbose_name="Alternative Text for The Thumbnail Picture", max_length=500, null=False, blank=False, default="Lorem ipsum", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).",)
    payment_link = models.URLField(max_length=1000, null=True, blank=True, verbose_name="Payment Link", help_text="Add a your payment link.<br><strongNote:</strong> You can use iyzico if you are in Turkey and Stripe payments if you are in North America.")

    def upload_cover_page_image(self, field_attname):
        """A function which generates dynamic paths for service images."""

        return f'services/{self.book_title}/{self.cover_page_image}'

    cover_page_image = models.ImageField(verbose_name="Cover Page Image", null=False, blank=False, upload_to=upload_cover_page_image, default="assets/default.jpg", help_text="<strong>Note: </strong><li>There is no specific required dimension.</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li><li>Make sure the file size is not over 30MB.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    cover_page_image_alt = models.TextField(verbose_name="Alternative Text for The Cover Page Image", max_length=500, null=False, blank=False, default="Lorem ipsum", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).",)

    def upload_table_of_contents_image(self, field_attname):
        """A function which generates dynamic paths for service images."""

        return f'services/{self.book_title}/{self.table_of_contents_image}'

    table_of_contents_image = models.ImageField(verbose_name="Table of Contents Image", null=True, blank=True, upload_to=upload_table_of_contents_image, help_text="<strong>Note: </strong><li>There is no specific required dimension.</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li><li>Make sure the file size is not over 30MB.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    table_of_contents_image_alt = models.TextField(verbose_name="Alternative Text for The Table of Contents Image", max_length=500, null=False, blank=False, default="Lorem ipsum", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).",)

    def upload_copyright_page_image(self, field_attname):
        """A function which generates dynamic paths for service images."""

        return f'services/{self.book_title}/{self.copyright_page_image}'

    copyright_page_image = models.ImageField(verbose_name="Copyright Page Image", null=True, blank=True, upload_to=upload_copyright_page_image, help_text="<strong>Note: </strong><li>There is no specific required dimension.</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li><li>Make sure the file size is not over 30MB.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    copyright_page_image_alt = models.TextField(verbose_name="Alternative Text for The Copyright Page Image", max_length=500, null=False, blank=False, default="Lorem ipsum", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).",)
    publishing_date = models.DateField(verbose_name="Publishing Date", auto_now_add=False, null=True, blank=True, help_text="Please use the fallowing format: YYYY-MM-DD")

    class Meta:

        verbose_name_plural = "Books Page Book"

    def __str__(self):
        """A function which returns a string which will represent the object."""

        return self.book_title

    def get_absolute_url(self):
        """A function which returns the url to access a particular service instance."""

        return reverse('book-detail', args=[str(self.id)])

class BooksPageVisit(models.Model):

    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now)
    screen_width = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Width")
    screen_height = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Height")
    
    class Meta:

        verbose_name_plural = 'Books Page Visit Information'
        ordering = ['-visit_time']

class BookDetailPageVisit(models.Model):

    uuid = models.CharField(max_length=500, null=False, blank=False, verbose_name="Universal Unique Identifier",)
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now,)
    screen_width = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Width",)
    screen_height = models.PositiveIntegerField(null=True, blank=True, verbose_name="Screen Height",)

    class Meta:

        verbose_name_plural = 'Book Detail Page Visit Information'
        ordering = ['-visit_time']