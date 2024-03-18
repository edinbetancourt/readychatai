from django.shortcuts import redirect
from django.views.generic import View

from todo.models import Task


class DeleteTask(View):
    """ Delete task """

    def post(self, request):
        task_id = request.POST.get('task_id')
        if task_id:
            Task.objects.filter(id=task_id).delete()

        return redirect('listtask')
