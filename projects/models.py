from django.db import models

class Project(models.Model):

    CATEGORY = [

        ("Residential","Residential"),
        ("Commercial","Commercial"),
        ("Villa","Villa"),

    ]

    title = models.CharField(max_length=200)

    category = models.CharField(max_length=50, choices=CATEGORY)

    location = models.CharField(max_length=100)

    description = models.TextField()

    cover_image = models.ImageField(upload_to="projects/")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(upload_to="project_gallery/")