from django.contrib.auth.models import AbstractUser
from django.db import models


class Tag(models.Model):
    tag_name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return f"{self.tag_name}"


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    task_status = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["task_status", "-datetime"]

    def __str__(self):
        return f"{self.content}"


class User(AbstractUser):
    pass
