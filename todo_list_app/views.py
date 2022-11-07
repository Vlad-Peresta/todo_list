from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from todo_list_app.forms import TaskForm
from todo_list_app.models import Task, Tag


class Index(generic.ListView):
    model = Task
    template_name = "todo_list_app/index.html"


class TaskCreationView(generic.CreateView):
    # model = Task
    # fields = "__all__"
    form_class = TaskForm
    template_name = "todo_list_app/task_form.html"
    success_url = reverse_lazy("todo_list_app:index")


class TaskUpdateView(generic.UpdateView):
    form_class = TaskForm
    template_name = "todo_list_app/task_form.html"
    success_url = reverse_lazy("todo_list_app:index")
    queryset = Task.objects


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list_app:index")


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo_list_app/tag_list.html"


class TagCreationView(generic.CreateView):
    # form_class = TaskForm
    model = Tag
    fields = "__all__"
    # template_name = "todo_list_app/tag_form.html"
    success_url = reverse_lazy("todo_list_app:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list_app:tag-list")
    template_name = "todo_list_app/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list_app:tag-list")


def change_task_status(request, pk):
    task = Task.objects.get(id=pk)

    if task.task_status:
        task.task_status = False
    else:
        task.task_status = True
    task.save()

    return HttpResponseRedirect(reverse_lazy("todo_list_app:index"))
