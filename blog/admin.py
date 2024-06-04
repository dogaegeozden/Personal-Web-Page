# LIBRARIES
from django.contrib import admin

# MODELS
from .models import (
    BlogPageMetaDescription,
    BlogPageBlogPost,
    BlogPageComment,
    BlogPageVisit,
    BlogPagePostDetailPageVisit,
    BlogPagePostLike,
    BlogPageShareClick,
)



##############################

# BLOG PAGE

##############################


@admin.register(BlogPageMetaDescription)
class BlogPageMetaDescriptionAdmin(admin.ModelAdmin):

    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',)
        }),
    )

@admin.register(BlogPageBlogPost)
class BlogPageBlogPostAdmin(admin.ModelAdmin):

    list_display = ('title', 'date',)
    list_filter = ('title', 'date',)
    readonly_fields=('id',)

    fieldsets = (
        ('Post Information & Content', {
            'fields': ('title', 'id', 'post_type', 'date', 'image', 'youtube_url', 'video', 'para1', 'para2', 'para3', 'para4', 'para5', 'para6', 'para7',)
        }),
        ('SEO (Search Engine Optimization) | Alt (Alternative Text): To make pictures accessable with texts', {
            'fields': ('alt',)
        }),
    )

@admin.register(BlogPageComment)
class BlogPageCommentAdmin(admin.ModelAdmin):

    readonly_fields=('post', 'commenter_name', 'text', 'comment_time', 'ip_address', 'user_agent',)

    fieldsets = (
        ('Comments', {
            'fields': ('post', 'commenter_name', 'text', 'comment_time', 'ip_address', 'user_agent',)
        }),
    )

@admin.register(BlogPageVisit)
class BlogPageVisitAdmin(admin.ModelAdmin):

    readonly_fields = ('ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height')

    fieldsets = (
        ('Blog Page Visit Information', {
            'fields': ('ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height')
        }),
    )

@admin.register(BlogPagePostDetailPageVisit)
class BlogPagePostDetailPageVisitAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid', 'ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height')

    fieldsets = (
        ('Post Detail Page\'s Visitors\' Information', {
            'fields': ('uuid', 'ip_address', 'visit_time', 'user_agent', 'screen_width', 'screen_height')
        }),
    )

@admin.register(BlogPagePostLike)
class BlogPagePostLikeAdmin(admin.ModelAdmin):
    readonly_fields = ('post', 'ip_address', 'user_agent', 'like_time', 'like_status',)

    fieldsets = (
        ('Post Detail Page\'s Visitors\' Information', {
            'fields': ('post', 'ip_address', 'like_time', 'user_agent', 'like_status',)
        }),
    )

@admin.register(BlogPageShareClick)
class BlogPageShareClickAdmin(admin.ModelAdmin):

    readonly_fields = ('uuid', 'ip_address', 'user_agent', 'click_time', 'platform_choice',)

    fieldsets = (
        ('Post Share Buttons\' Click Information', {
            'fields': ('uuid', 'ip_address', 'user_agent', 'click_time', 'platform_choice',)
        }),
    )
