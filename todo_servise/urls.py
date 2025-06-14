from django.urls import path

from todo_servise.views import TodoListView, TaskCreatedView, switch_done_or_not_done, TaskUpdateView, TaskDeleteView, \
    TagListView, TagCreatedView, TagUpdateView, TagDeleteView

urlpatterns = [
    path("", TodoListView.as_view(), name="todo-list"),
    path("task_created/", TaskCreatedView.as_view(), name="task-created"),
    path("task_done_or_not/<int:pk>/", switch_done_or_not_done, name="task-done-or-not"),
    path("update_task/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("delete_task/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tag_create/", TagCreatedView.as_view(), name="tag-create"),
    path("tag_update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tag_delete/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),

]

app_name = "todo_servise"