# LIBRARIES
from django.contrib import admin

# MODELS
from .models import (
    PrivacyPolicyPageMetaDescription,
    PrivacyPolicyPageVisit,
    PrivacyPolicy,

    TermsAndConditionsPageMetaDescription,
    TermsAndConditionsPageVisit,
    TermsAndConditions,
)



##############################

# PRIVACY POLICY PAGE

##############################

@admin.register(PrivacyPolicyPageMetaDescription)
class PrivacyPolicyPageMetaDescriptionAdmin(admin.ModelAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',)
        }),
    )

@admin.register(PrivacyPolicyPageVisit)
class PrivacyPolicyPageVisitAdmin(admin.ModelAdmin):

    readonly_fields = ('ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height',)

    fieldsets = (
        ('Privacy Policy Page\'s Visitor\'s Information', {
            'fields': ('ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height',)
        }),
    )

@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Privacy Policy', {
            'fields': ('effective_date', 'section_1_title', 'section_1_text', 'section_2_title', 'section_2_text', 'section_3_title', 'section_3_text', 'section_4_title', 'section_4_text', 'section_5_title', 'section_5_text', 'section_6_title', 'section_6_text', 'section_7_title', 'section_7_text', 'section_8_title', 'section_8_text', 'section_9_title', 'section_9_text', 'section_10_title', 'section_10_text', 'section_11_title', 'section_11_text', 'section_12_title', 'section_12_text', 'references_text',)
        }),
    )



##############################

# TERMS AND CONDITIONS PAGE

##############################

@admin.register(TermsAndConditionsPageMetaDescription)
class TermsAndConditionsPageMetaDescriptionAdmin(admin.ModelAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',)
        }),
    )

@admin.register(TermsAndConditionsPageVisit)
class TermsAndConditionsPageVisitAdmin(admin.ModelAdmin):

    readonly_fields = ('ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height',)

    fieldsets = (
        ('Privacy Policy Page\'s Visitor\'s Information', {
            'fields': ('ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height',)
        }),
    )

@admin.register(TermsAndConditions)
class TermsAndConditionsAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Privacy Policy', {
            'fields': ('effective_date', 'section_1_title', 'section_1_text', 'section_2_title', 'section_2_text', 'section_3_title', 'section_3_text', 'section_4_title', 'section_4_text', 'section_5_title', 'section_5_text', 'section_6_title', 'section_6_text', 'section_7_title', 'section_7_text', 'section_8_title', 'section_8_text', 'section_9_title', 'section_9_text', 'section_10_title', 'section_10_text', 'section_11_title', 'section_11_text', 'section_12_title', 'section_12_text', 'references_text',)
        }),
    )
