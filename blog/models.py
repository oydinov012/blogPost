
from django.db import models
from django.core.validators import FileExtensionValidator, MaxLengthValidator
from config.settings import DATABASES
from  users.models import CustomUser
"""
Postlarda bo‘lishi kerak





Sarlavhasi (title)



Matni (content)



Rasm (image)



Bo‘limi (category)



Teglari (tags)"""



DASTURLASH,XABARLAR,TALIM,MOLIYA,TIBBIYOT = ('dasturlash','xabarlar','talim','moliya','tibbiyot' )
    

class Post(models.Model):
    CATEGORY_CHOISES=(
        (DASTURLASH,DASTURLASH),
        (XABARLAR,XABARLAR),
        (TALIM,TALIM),
        (MOLIYA,MOLIYA),
        (TIBBIYOT,TIBBIYOT)
    )
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name='post_users')
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.CharField(max_length=200)
    category = models.CharField(max_length=200,choices=CATEGORY_CHOISES ,default=XABARLAR)
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


