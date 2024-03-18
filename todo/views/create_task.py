from django.views.generic import CreateView
from django.shortcuts import redirect

from todo.models import Task


class CreateTask(CreateView):
    """ Create task """
    model = Task
    template_name = 'list_task.html'
    fields = ('title', 'description',)
    success_url = 'listtask'

    def form_invalid(self, form):
            return redirect('listtask')
