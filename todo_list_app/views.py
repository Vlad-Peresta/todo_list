from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_list_app.forms import TaskCreationForm
from todo_list_app.models import Task, Tag


class Index(generic.ListView):
    model = Task
    template_name = "todo_list_app/index.html"


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo_list_app/tag_list.html"


class TaskUpdateView(generic.UpdateView):
    model = Task


class TaskCreationView(generic.CreateView):
    model = Task
    fields = ["content", "deadline"]
    success_url = reverse_lazy("todo_list_app:index")
