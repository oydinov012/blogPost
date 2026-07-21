from django.contrib import admin
from comment.models import Comment

class CommentAdmin(admin.ModelAdmin):
    search_fields = ('user__username','blog__title', 'comment')
    list_display = ('user', 'blog', 'comment')

admin.site.register(Comment, CommentAdmin)