from django.urls import path

from todo_list_app.views import (
    Index,
    TagListView,
    TaskUpdateView,
    TaskCreationView,
    TagCreationView,
    TagUpdateView,
    TaskDeleteView,
    TagDeleteView,
    change_task_status,
)

app_name = "todo_list_app"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("tasks/create/", TaskCreationView.as_view(), name="task-create"),
    path("tasks/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tasks/<int:pk>/change-task_status",
        change_task_status,
        name="change_task_status",
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreationView.as_view(), name="tag-create"),
    path("tags/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]
