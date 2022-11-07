"""Todo_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path

from todo_list_app.views import Index, TagListView, TaskUpdateView, TaskCreationView, TagCreationView, TagUpdateView, \
    TaskDeleteView, TagDeleteView, change_task_status

app_name = "todo_list_app"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("tasks/create/", TaskCreationView.as_view(), name="task-create"),
    path("tasks/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/change-task_status", change_task_status, name="change_task_status"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreationView.as_view(), name="tag-create"),
    path("tags/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]
