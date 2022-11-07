from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    task_status = models.BooleanField(default=False)


class Tag(models.Model):
    tag_name = models.CharField(max_length=63)
    tasks = models.ManyToManyField(Task, related_name="tags")
