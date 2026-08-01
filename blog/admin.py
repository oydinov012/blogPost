from django.contrib import admin
from blog.models import  Post,  PostMedia


class BlogImageInline(admin.TabularInline):
    model = PostMedia
    extra = 1



class PostAdmin(admin.ModelAdmin):
    search_fields = ('user__username', 'title', 'content', 'category', 'tags', "is_approved")
    list_display= ('user', 'title', 'content')
    inlines = [BlogImageInline]

admin.site.register(Post, PostAdmin)