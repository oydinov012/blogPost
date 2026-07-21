from django.contrib import admin
from blog.models import Category, Post, Tags

class CategoryAdmin(admin.ModelAdmin):
    pass

class TagsAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    search_fields = ('user__username', 'title', 'content', 'category__name', 'tags__name', "is_approved")
    list_display= ('user', 'title', 'content')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Post, PostAdmin)