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
    image = models.ImageField(default='media/blog.jpeg', upload_to='media-files', validators=[
        FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts_category')

    tags = models.ManyToManyField(Tags,blank=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title


