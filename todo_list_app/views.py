from django.shortcuts import render
from django.views import generic

from todo_list_app.models import Task


class Index(generic.ListView):
    model = Task
    paginate_by = 5
