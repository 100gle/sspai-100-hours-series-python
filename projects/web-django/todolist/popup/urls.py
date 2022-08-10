from django.urls import path

from .views import about, create_task, delete_task, index, query_all_tasks, update_task

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("tasks/", query_all_tasks, name="tasks"),
    path("tasks/create/", create_task, name="create_task"),
    path("tasks/update/<int:task_id>/", update_task, name="update_task"),
    path("tasks/delete/<int:task_id>/", delete_task, name="delete_task"),
]
