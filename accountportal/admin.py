# LIBRARIES
from django.contrib import admin

# Importing models
from .models import (
    RegisterPageMetaDescription,
    RegisterPageVisit,

    LoginPageMetaDescription,
    LogoutPageMetaDescription,
    
    PasswordResetCompletePageMetaDescription,
    PasswordResetConfirmPageMetaDescription,
    PasswordResetDonePageMetaDescription,
    PasswordResetFormPageMetaDescription,
    
    Profile,
    ProfilePageVisit,
)



##############################

# ACCOUNT PORTAL REGISTRATIONS

##############################

@admin.register(RegisterPageMetaDescription)
class RegisterPageMetaDescriptionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',) # You should put "," after first item or else python won't recognize it as tuple.
        }),
    )

@admin.register(RegisterPageVisit)
class RegisterPageVisitAdmin(admin.ModelAdmin):
    readonly_fields = ('ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height')
    fieldsets = (
        ('Register Page Visit Information', {
            'fields': ('ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height')
        }),
    )


@admin.register(LoginPageMetaDescription)
class LoginPageMetaDescriptionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',) # You should put "," after first item or else python won't recognize it as tuple.
        }),
    )

@admin.register(LogoutPageMetaDescription)
class LogoutPageMetaDescriptionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',)
        }),
    )

@admin.register(PasswordResetCompletePageMetaDescription)
class PasswordResetCompletePageMetaDescriptionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',)
        }),
    )

@admin.register(PasswordResetConfirmPageMetaDescription)
class PasswordResetConfirmPageMetaDescriptionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',)
        }),
    )

@admin.register(PasswordResetDonePageMetaDescription)
class PasswordResetDonePageMetaDescriptionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',)
        }),
    )

@admin.register(PasswordResetFormPageMetaDescription)
class PasswordResetFormPageMetaDescriptionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',) 
        }),
    )

@admin.register(Profile)
class ProfilePageProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('User Profile', {
            'fields': ('user', 'full_name', 'image',)
        }),
    )

@admin.register(ProfilePageVisit)
class ProfilePageVisitAdmin(admin.ModelAdmin):
    readonly_fields = ('username', 'ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height')
    fieldsets = (
        ('Profile Page Visit Information', {
            'fields': ('username', 'ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height')
        }),
    )
