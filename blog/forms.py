from dataclasses import field, fields
from pyexpat import model
from unicodedata import category

from django import forms
from .models import Post, Category, Tags

class TagsForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ("name",)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name",)

class PostForm(forms.ModelForm):
    category = CategoryForm()
    tags = TagsForm()

    class Meta:
        model = Post
        fields = ('user', 'title', 'content', 'image', 'category', 'tags', 'is_approved')