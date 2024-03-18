from django.views.generic import CreateView

from todo.models import Task


class CreateTask(CreateView):
    """ Create task """
    model = Task
    template_name = 'create_task.html'
    fields = ('title', 'description',)
    success_url = 'listtask'
