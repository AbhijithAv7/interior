from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class BlogPost(models.Model):

    CATEGORY_CHOICES = [
        ('Interior Design', 'Interior Design'),
        ('Living Room', 'Living Room'),
        ('Bedroom', 'Bedroom'),
        ('Kitchen', 'Kitchen'),
        ('Office', 'Office'),
        ('Architecture', 'Architecture'),
        ('Tips & Ideas', 'Tips & Ideas'),
    ]

    title = models.CharField(max_length=200)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    featured_image = models.ImageField(
        upload_to='blog/'
    )

    excerpt = models.TextField(
        max_length=300,
        blank=True
    )

    content = models.TextField()

    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    is_published = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title