from turtle import update

from django.db import models
from django.core.validators import FileExtensionValidator, MaxLengthValidator
from  users.models import CustomUser
"""
Postlarda bo‘lishi kerak





Sarlavhasi (title)



Matni (content)



Rasm (image)



Bo‘limi (category)



Teglari (tags)"""


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Tags(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


    

class Post(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name='post_users')
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts_category')

    tags = models.ManyToManyField(Tags,blank=True)
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    @property
    def cover_media(self):
        return self.media.filter(is_cover=True).first() or self.media.first() # type: ignore

    def __str__(self):
        return f"{self.user}ning {self.title} nomli posti"

class PostMedia(models.Model):

    IMAGE = "image"
    VIDEO = "video"
    FILE = "file"

    MEDIA_TYPES = [
        (IMAGE, "Image"),
        (VIDEO, "Video"),
        (FILE, "File"),
    ]

    blog = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="media"
    )

    media_type = models.CharField(
        max_length=20,
        choices=MEDIA_TYPES,
        default=IMAGE

    )

    file = models.FileField(default='media/blog.jpeg',upload_to="blog_media/",)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now=True)
    is_cover = models.BooleanField(default=False)


