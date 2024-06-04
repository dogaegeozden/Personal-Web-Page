# LIBRARIES
from django.contrib import admin

# MODELS
from .models import (

    GlobalBrandIdentity,
    GlobalSocialMediaLinks,
    GlobalContactInformation,
    GlobalSocialMediaButtonClick,
    GlobalDocumentClickCoordinate,
    GlobalMouseTrace,
    GlobalKeystroke,
    GlobalSubscription,
    GlobalUnsubscribeLink,

    HomePageMetaDescription,
    HomePageProfilePic,
    HomePageBio,
    HomePageToolOrLanguage,
    HomePageToolsOrLanguagesMainContent,
    HomePageToolOrLanguageImageClick,
    HomePageActivity,
    HomePageVisit,
    HomePageActivityImageClick,
    HomePageProfilePictureClick,
    HomePageToolsAndLanguagesImageClick,
    HomePagePartnersSectionTextContent,
    HomePagePartner,

    PortfolioPageMetaDescription,
    PortfolioPagePhotoGridColumn1Image,
    PortfolioPagePhotoGridColumn2Image,
    PortfolioPagePhotoGridColumn3Image,
    PortfolioPagePhotoGridColumn4Image,
    PortfolioPageSlideShowVideo,
    PortfolioPageWebDevelopment,
    PortfolioPageVisit,
    PortfolioPageGraphicDesignProjClickData,
    PortfolioPageWebDevProjClickData,

    CertificationsPageMetaDescription,
    CertificationsPageCertification,
    CertificationsPageVisit,
    CertificationsPageCertificationClick,

    ResumesPageMetaDescription,
    ResumesPageAboutCurrentPosition,
    ResumesPageResume,
    ResumesPageExperience,
    ResumesPageEducation,
    ResumesPageVisit,
    ResumesPageResumeFileClicks,

    ContactPageMetaDescription,
    ContactPageContactPPic,
    ContactPageMessage,
    ContactPageVisit,

)



##############################

# GLOBAL REGISTRATIONS

##############################

@admin.register(GlobalUnsubscribeLink)
class GlobalUnsubscribeLinkAdmin(admin.ModelAdmin):

    readonly_fields = ('subscription', 'token',)

    fieldsets = (
        ('Brand Identity', {
            'fields': ('subscription', 'token',)
        }),
    )

@admin.register(GlobalBrandIdentity)
class GlobalBrandIdentityAdmin(admin.ModelAdmin):
    
    fieldsets = (
        ('Brand Identity', {
            'fields': ('icon', 'logo', 'copy_right_text', 'slogan', 'alt',)
        }),
    )


@admin.register(GlobalSocialMediaLinks)
class GlobalSocialMediaLinksAdmin(admin.ModelAdmin):
    
    fieldsets = (
        ('Social Media Links', {
            'fields': ('linkedin', 'instagram', 'facebook', 'github', 'online_store', 'x', 'tiktok', 'youtube', 'slideshare',)
        }),
    )


@admin.register(GlobalContactInformation)
class GlobalContactInformationAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Contact Information', {
            'fields': ('email', 'freelancer', 'upwork', 'fiverr', 'phone_number', 'address',)
        }),
    )


@admin.register(GlobalSocialMediaButtonClick)
class GlobalSocialMediaButtonClickAdmin(admin.ModelAdmin):

    readonly_fields = ('ip_address', 'click_time', 'user_agent', 'platform_choice', 'page_url',)

    fieldsets = (
        ('Social Media Button Click', {
            'fields': ('ip_address', 'click_time', 'user_agent', 'platform_choice', 'page_url',)
        }),
    )


@admin.register(GlobalDocumentClickCoordinate)

class GlobalDocumentClickCoordinateAdmin(admin.ModelAdmin):

    readonly_fields = ('ip_address', 'user_agent', 'click_time', 'screen_width', 'screen_height', 'x_coordinate', 'y_coordinate', 'page_url',)

    fieldsets = (
        ('Document Click Coordinate', {
            'fields': ('ip_address', 'user_agent', 'click_time', 'screen_width', 'screen_height', 'x_coordinate', 'y_coordinate', 'page_url',)
        }),
    )


@admin.register(GlobalMouseTrace)

class GlobalMouseTraceAdmin(admin.ModelAdmin):

    readonly_fields = ('ip_address', 'user_agent', 'movement_time', 'screen_width', 'screen_height', 'x_coordinate', 'y_coordinate', 'page_url',)

    fieldsets = (
        ('Document Click Coordinate', {
            'fields': ('ip_address', 'user_agent', 'movement_time', 'screen_width', 'screen_height', 'x_coordinate', 'y_coordinate', 'page_url',)
        }),
    )


@admin.register(GlobalKeystroke)

class GlobalKeystrokeAdmin(admin.ModelAdmin):

    readonly_fields = ('ip_address', 'user_agent', 'pressing_time', 'keystroke', 'page_url',)

    fieldsets = (
        ('Keystroke', {
            'fields': ('ip_address', 'user_agent', 'pressing_time', 'keystroke', 'page_url',)
        }),
    )

@admin.register(GlobalSubscription)

class GlobalSubscriptionAdmin(admin.ModelAdmin):

    readonly_fields=('email', 'ip_address', 'user_agent', 'subscribing_time',) 
    fieldsets = (
        ('Message', {
            'fields': ('email', 'ip_address', 'user_agent', 'subscribing_time',)
        }),
    )



##############################

# HOME PAGE

##############################

@admin.register(HomePageMetaDescription)

class HomePageMetaDescriptionAdmin(admin.ModelAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',)
        }),
    )


@admin.register(HomePageProfilePic)

class HomePageProfilePic(admin.ModelAdmin):

    fieldsets = (
        ('Profile Picture', {
            'fields': ('image',)
        }),

        ('SEO (Search Engine Optimization) | Alt (Alternative Text): To make pictures accessable with texts', {
            'fields': ('alt',)
        }),
    )


@admin.register(HomePageBio)

class HomePageBioAdmin(admin.ModelAdmin):

    fieldsets = (
        ('BIO (Biography)', {
            'fields': ('text',)
        }),
    )


@admin.register(HomePageToolsOrLanguagesMainContent)

class HomePageToolsAndLanguagesMainContentAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Tools And Languages Section\'s Main Visual', {
            'fields': ('title', 'image', 'alt',)
        }),
    )


@admin.register(HomePageToolOrLanguage)

class HomePageToolOrLanguageAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Tool or Language', {
            'fields': ('title', 'icon_url', 'icon_file', 'alt',)
        }),
    )

@admin.register(HomePageToolOrLanguageImageClick)

class HomePageToolOrLanguageImageClickAdmin(admin.ModelAdmin):

    readonly_fields = ('ip_address', 'user_agent', 'click_time', 'tool_or_language_choice',)

    fieldsets = (
        ('Social Media Button Click', {
            'fields': ('ip_address', 'user_agent', 'click_time', 'tool_or_language_choice',)
        }),
    )


@admin.register(HomePageActivity)

class HomePageActivityAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Activity Information & Content', {
            'fields': ('title', 'description', 'image')
        }),

        ('SEO (Search Engine Optimization) | Alt (Alternative Text): To make pictures accessable with texts', {
            'fields': ('alt',)
        }),
    )


@admin.register(HomePageVisit)

class HomePageVisitAdmin(admin.ModelAdmin):

    readonly_fields = ('ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height',)

    fieldsets = (
        ('Main Page Visitor\'s Information', {
            'fields': ('ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height',)
        }),
    )


@admin.register(HomePageActivityImageClick)

class HomePageActivityImageClickAdmin(admin.ModelAdmin):

    readonly_fields = ('ip_address', 'click_time', 'user_agent', 'activity_image_choice',)

    fieldsets = (
        ('Activity Image Click', {
            'fields': ('ip_address', 'click_time', 'user_agent', 'activity_image_choice',)
        }),
    )


@admin.register(HomePageProfilePictureClick)

class HomePageProfilePictureClickAdmin(admin.ModelAdmin):

    readonly_fields = ('ip_address', 'click_time', 'user_agent', 'profile_picture_choice',)

    fieldsets = (
        ('Profile Picture Click', {
            'fields': ('ip_address', 'click_time', 'user_agent', 'profile_picture_choice',)
        }),
    )


@admin.register(HomePageToolsAndLanguagesImageClick)

class HomePageToolsAndLanguagesImageClickAdmin(admin.ModelAdmin):

    readonly_fields = ('ip_address', 'click_time', 'user_agent', 'tools_and_languages_image_choice',)

    fieldsets = (
        ('Tools And Languages Image Click', {
            'fields': ('ip_address', 'click_time', 'user_agent', 'tools_and_languages_image_choice',)
        }),
    )


@admin.register(HomePagePartnersSectionTextContent)

class HomePagePartnersSectionTextContentAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Client Section Text Content', {
            'fields': ('title', 'text',)
        }),
    )


@admin.register(HomePagePartner)

class HomePagePartnerAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Client Logo', {
            'fields': ('logo', 'logo_alt',)
        }),

    )



##############################

# PORTFOLIO PAGE

##############################

@admin.register(PortfolioPageMetaDescription)

class MetaDescriptionAdmin(admin.ModelAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',)
        }),
    )


@admin.register(PortfolioPagePhotoGridColumn1Image)

class PortfolioPagePhotoGridColumn1ImageAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Column 1 Image', {
            'fields': ('img', 'img_alt',)
        }),
    )


@admin.register(PortfolioPagePhotoGridColumn2Image)

class PortfolioPagePhotoGridColumn2ImageAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Column 2 Image', {
            'fields': ('img', 'img_alt',)
        }),
    )


@admin.register(PortfolioPagePhotoGridColumn3Image)

class PortfolioPagePhotoGridColumn3ImageAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Column 3 Image', {
            'fields': ('img', 'img_alt',)
        }),
    )


@admin.register(PortfolioPagePhotoGridColumn4Image)

class PortfolioPagePhotoGridColumn4ImageAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Column 4 Image', {
            'fields': ('img', 'img_alt',)
        }),
    )


@admin.register(PortfolioPageSlideShowVideo)

class PortfolioPageVideoSlideShowAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Video Slide Show Video', {
            'fields': ('video', 'video_alt',)
        }),
    )


@admin.register(PortfolioPageWebDevelopment)

class PortfolioPageWebDevelopmentAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Web Development', {
            'fields': ('title', 'preview_image', 'web_page_link',)
        }),
    )


@admin.register(PortfolioPageVisit)

class PortfolioPageVisitAdmin(admin.ModelAdmin):

    readonly_fields = ('ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height',)

    fieldsets = (
        ('Portfolio Page\'s Visitor\'s Information', {
            'fields': ('ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height',)
        }),
    )


@admin.register(PortfolioPageGraphicDesignProjClickData)

class GraphicDesignProjClickDataAdmin(admin.ModelAdmin):

    readonly_fields = ('project_choice', 'ip_address', 'click_time', 'user_agent',)

    fieldsets = (
        ('Portfolio Page\'s Visitor\'s Information', {
            'fields': ('project_choice', 'ip_address', 'click_time', 'user_agent',)
        }),
    )


@admin.register(PortfolioPageWebDevProjClickData)

class WebDevProjClickDataAdmin(admin.ModelAdmin):

    readonly_fields = ('project_choice', 'ip_address', 'click_time', 'user_agent',)

    fieldsets = (
        ('Portfolio Page\'s Visitor\'s Information', {
            'fields': ('project_choice', 'ip_address', 'click_time', 'user_agent',)
        }),
    )



##############################

# CERTIFICATIONS PAGE

##############################

@admin.register(CertificationsPageMetaDescription)

class CertificationsPageMetaDescriptionAdmin(admin.ModelAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',)
        }),
    )

@admin.register(CertificationsPageCertification)

class CertificationsPageCertificationAdmin(admin.ModelAdmin):

    list_display = ('title', 'topic')

    list_filter = ('title', 'topic')

    fieldsets = (
        ('Certification', {
            'fields': ('title', 'topic', 'digital_copy', 'digital_copy_url', 'issuer', 'issue_date', 'expiry_date',)
        }),
    )


@admin.register(CertificationsPageVisit)

class CertificationsPageVisit(admin.ModelAdmin):

    readonly_fields = ('ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height')

    fieldsets = (
        ('Main Page Visitor\'s Information', {
            'fields': ('ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height',)
        }),
    )


@admin.register(CertificationsPageCertificationClick)

class CertificationsPageCertificationClickAdmin(admin.ModelAdmin):

    readonly_fields = ('ip_address', 'click_time', 'user_agent', 'certification_choice',)

    fieldsets = (
        ('Social Media Button Click', {
            'fields': ('ip_address', 'click_time', 'user_agent', 'certification_choice',)
        }),
    )



##############################

# RESUMES PAGE

##############################

@admin.register(ResumesPageResume)

class ResumesPageResumeAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Resume Information & Content', {
            'fields': ('field_name', 'resume_name', 'file',)
        }),
    )


@admin.register(ResumesPageMetaDescription)

class ResumesPageMetaDescriptionAdmin(admin.ModelAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',)
        }),
    )


@admin.register(ResumesPageAboutCurrentPosition)

class ResumesPageAboutCurrentPositionAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Text About Your Current Position in Your Career', {
            'fields': ('text',)
        }),
    )


@admin.register(ResumesPageExperience)

class ExperienceAdmin(admin.ModelAdmin):

    list_display = ('job_title', 'company_name', 'start_date', 'end_date', 'working_status')

    list_filter = ('job_title', 'company_name', 'start_date', 'end_date', 'working_status')

    fieldsets = (

        ('Job Information', {
            'fields': ('job_title', 'company_name', 'text', 'header', 'list_item_1', 'list_item_2', 'list_item_3', 'list_item_4', 'list_item_5','img_1', 'img_2', 'img_3', 'img_4', 'img_5', 'img_6', 'img_7', 'img_8', 'img_9', 'img_10',)
        }),

        ('Working Status', {
            'fields': ('start_date', 'end_date', 'working_status')
        }),

    )


@admin.register(ResumesPageEducation)

class ResumesPageEducationAdmin(admin.ModelAdmin):

    fieldsets = (

        ('Education Information', {
            'fields': ('name', 'city', 'province', 'start_date', 'end_date', 'major', 'diploma', 'para',)
        }),

        ('SEO (Search Engine Optimization) | Alt (Alternative Text): To make pictures accessable with texts', {
            'fields': ('alt',)
        }),

    )


@admin.register(ResumesPageVisit)

class ResumesPageVisitAdmin(admin.ModelAdmin):

    readonly_fields = ('ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height',)

    fieldsets = (
        ('Resumes Page Visitor Information', {
            'fields': ('ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height',)
        }),
    )


@admin.register(ResumesPageResumeFileClicks)

class ResumesPageResumeFileClicksAdmin(admin.ModelAdmin):

    readonly_fields = ('resume_choice', 'ip_address', 'click_time', 'user_agent',)

    fieldsets = (
        ('Resume File Click Information', {
            'fields': ('resume_choice', 'ip_address', 'click_time', 'user_agent',)
        }),
    )



##############################

# CONTACT PAGE

##############################

@admin.register(ContactPageMetaDescription)

class ContactPageMetaDescriptionAdmin(admin.ModelAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',)
        }),
    )


@admin.register(ContactPageContactPPic)

class ContactPageContactPPicAdmin(admin.ModelAdmin):

    fieldsets = (

        ('Contact Page Picture', {
            'fields': ('image',)
        }),

        ('SEO (Search Engine Optimization) | Alt (Alternative Text): To make pictures accessable with texts', {
            'fields': ('alt',)
        }),

    )


@admin.register(ContactPageMessage)

class ContactPageMessageAdmin(admin.ModelAdmin):
    
    readonly_fields=('first_name', 'last_name', 'email', 'phone_number', 'message', 'message_sending_time', 'ip_address', 'user_agent',) # These fields cannot be edited from admin page.
    
    fieldsets = (
        ('Message', {
            'fields': ('first_name', 'last_name', 'email', 'phone_number', 'message', 'message_sending_time', 'ip_address', 'user_agent',)
        }),    
    )


@admin.register(ContactPageVisit)

class ContactPageVisitAdmin(admin.ModelAdmin):

    readonly_fields = ('ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height')

    fieldsets = (
        ('Post Detail Page Visitor\'s Information', {
            'fields': ('ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height',)
        }),
    )