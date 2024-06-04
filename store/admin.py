# LIBRARIES
from django.contrib import admin

# MODELS
from .models import (
    ServicesPageMetaDescription,
    ServicesPageMainContent,
    ServicesPageService,
    ServicesPageVisit,
    ServiceDetailPageVisit,

    BooksPageMetaDescription,
    BooksPageBook,
    BooksPageVisit,
    BookDetailPageVisit,
)



##############################

# SERVICES PAGE

##############################

@admin.register(ServicesPageMetaDescription)
class ServicesPageMetaDescriptionAdmin(admin.ModelAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',)
        }),
    )

@admin.register(ServicesPageMainContent)
class ServicesPageMainContentAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Services Page Main Content', {
            'fields': ('video', 'alt', 'para1', 'para2', 'para3',)
        }),
    )

@admin.register(ServicesPageService)
class ServicesPageServiceAdmin(admin.ModelAdmin):

    readonly_fields=('id',)

    fieldsets = (
        ('Service Information & Content', {
            'fields': ('id', 'slug', 'service_title', 'meta_description', 'short_summary', 'thumbnail_picture', 'alt_for_thumbnail_picture', 'call_to_action_sentence', 'process_chart', 'process_chart_alt', 'header1', 'image1', 'alt1', 'para1', 'para2', 'para3', 'header2', 'image2', 'alt2', 'para4', 'para5', 'para6', 'header3', 'image3', 'alt3', 'para7', 'para8', 'para9')
        }),
    )

@admin.register(ServicesPageVisit)
class ServicesPageVisitAdmin(admin.ModelAdmin):
    
    readonly_fields = ('ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height',)
    
    fieldsets = (
        ('Services Page Visit Information', {
            'fields': ('ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height',)
        }),
    )

@admin.register(ServiceDetailPageVisit)
class ServiceDetailPageVisitAdmin(admin.ModelAdmin):

    readonly_fields = ('uuid', 'ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height')

    fieldsets = (
        ('Service Detail Page\'s Visitor\'s Information', {
            'fields': ('uuid', 'ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height')
        }),
    )



##############################

# BOOKS PAGE

##############################

@admin.register(BooksPageMetaDescription)
class BooksPageMetaDescriptionAdmin(admin.ModelAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',)
        }),
    )

@admin.register(BooksPageBook)
class BooksPageBookAdmin(admin.ModelAdmin):

    readonly_fields=('id',)

    fieldsets = (
        ('Book Information & Content', {
            'fields': ('id', 'book_title', 'author', 'meta_description', 'short_summary', 'thumbnail_picture', 'thumbnail_pic_alt', 'call_to_action_sentence', 'payment_link', 'cover_page_image', 'cover_page_image_alt', 'table_of_contents_image', 'copyright_page_image', 'copyright_page_image_alt')
        }),
    )

@admin.register(BooksPageVisit)
class BooksPageVisitAdmin(admin.ModelAdmin):
    
    readonly_fields = ('ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height',)
    
    fieldsets = (
        ('Book Page Visit Information', {
            'fields': ('ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height',)
        }),
    )

@admin.register(BookDetailPageVisit)
class BookDetailPageVisitVisitAdmin(admin.ModelAdmin):

    readonly_fields = ('uuid', 'ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height')

    fieldsets = (
        ('Book Detail Page\'s Visitor\'s Information', {
            'fields': ('uuid', 'ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height')
        }),
    )