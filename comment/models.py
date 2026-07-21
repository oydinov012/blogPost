from django.db import models
from blog.models import Post

class Comment(models.Model):
    user = models.ForeignKey(
        'users.Customuser', 
        related_name='comment_users',
        on_delete=models.CASCADE
        )
    blog = models.ForeignKey(
        Post,
        related_name='post_comment',
        on_delete=models.CASCADE
    )
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)