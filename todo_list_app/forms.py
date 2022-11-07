from django import forms

from todo_list_app.models import Task


class TaskCreationForm(forms.ModelForm):
    model = Task

