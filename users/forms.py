from dataclasses import field, fields
from email.policy import default
from typing import Any

from django import forms
from .models import CustomUser


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username','last_name',"first_name","email",'password')

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user



class UserUpdateForm(forms.ModelForm):
    input_password= forms.CharField(max_length=20)
    
    class Meta:
        model = CustomUser
        fields = ('username','last_name',"first_name","email",'input_password',"phone_number", "photo")

    def save(self, commit=True):
            user = super().save(commit)
            user.set_password(self.cleaned_data['input_password'])
            user.save()
            return user
    