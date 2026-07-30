from pickle import TRUE

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment'] # Faqat comment maydoni ko'rsatiladi
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Fikringizni yozing...'})
        }


class CommentDeleteForm(forms.Form):
    tasdiqlash = forms.BooleanField(
        required=True,
        help_text='commentariyani ochirmoqchimisiz',
        label='ochirish'
    )