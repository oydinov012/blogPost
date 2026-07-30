
from django import forms
from .models import Post

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", forms.FileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class PostForm(forms.ModelForm):  # <--- BaseForm o'rniga ModelForm yoziladi
    media_files = MultipleFileField(
        required=False,
        label="Rasm yoki Videolar"
    )

    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'tags', 'media_files')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # 'multiple' atributini va Bootstrap klasslarini qo'shish
        self.fields['media_files'].widget.attrs.update({
            'multiple': True, 
            'class': 'form-control'
        })
        
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'rows': 5})
        self.fields['category'].widget.attrs.update({'class': 'form-select'})
        self.fields['tags'].widget.attrs.update({'class': 'form-select'})

class PostdeleteForm(forms.Form):
    tasdiqlash = forms.BooleanField(
        required=True,
        help_text='Ochirilgan Postni qayta tiklab bolmaydi',
        label="O'chirishni tasdiqlaysizmi"
    )