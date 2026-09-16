from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost

        fields = [
            'title',
            'category',
            'featured_image',
            'excerpt',
            'content',
            'is_published',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter blog title'
            }),

            'category': forms.Select(attrs={
                'class': 'form-input'
            }),

            'featured_image': forms.ClearableFileInput(attrs={
                'class': 'form-input'
            }),

            'excerpt': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Write a short description...',
                'rows': 4
            }),

            'content': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Write your blog content...',
                'rows': 12
            }),

            'is_published': forms.CheckboxInput(attrs={
                'class': 'form-checkbox'
            }),
        }