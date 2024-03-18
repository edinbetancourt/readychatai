from django.urls import path

from todo.views import create_task, list_task, delete_task, completed_task


urlpatterns = [
    path('createtask', create_task.CreateTask.as_view(), name='createtask'),
    path('listtask', list_task.ListTask.as_view(), name='listtask'),
    path('deletetask', delete_task.DeleteTask.as_view(), name='deletetask'),
    path('completedtask', completed_task.CompleteTask.as_view(), name ='completedtask'),
]
