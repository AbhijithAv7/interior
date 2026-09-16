from django import forms
from projects.models import Project
from projects.models import ProjectImage
from blog.models import BlogPost


class ProjectForm(forms.ModelForm):

    class Meta:

        model = Project

        fields = [

            "title",

            "category",

            "location",

            "description",

            "cover_image",

            

        ]


class GalleryForm(forms.ModelForm):

    class Meta:

        model = ProjectImage

        fields = [

            "project",

            "image",

        ]





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
                'placeholder': 'Short description of the blog',
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