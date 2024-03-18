from django.shortcuts import redirect
from django.views.generic import View

from todo.models import Task


class CompleteTask(View):
    """ Completed task """

    def post(self, request):
        completed_id = request.POST.get('completed_id')

        if completed_id:
            task = Task.objects.filter(id=completed_id).first()
            if task:
                if task.completed:
                    task.completed = False
                else:
                    task.completed = True
                
                task.save()

        return redirect('listtask')
