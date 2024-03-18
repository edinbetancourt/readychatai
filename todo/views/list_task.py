from django.views.generic import ListView

from todo.models import Task


class ListTask(ListView):
    """ List task """
    model = Task
    template_name = 'list_task.html'
    queryset = Task.objects.all().order_by('-created')
    paginate_by = 10
