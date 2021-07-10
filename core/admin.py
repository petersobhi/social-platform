from django.contrib import admin

from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('body', 'attachment', 'user')
    list_display_links = None  # Disable editing links

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request):
        return False


class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'post', 'user')
    list_display_links = None  # Disable editing links

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request):
        return False

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)