# DRF 
from rest_framework import viewsets

# Serializer
from api.serializer.todo import TodoSerializer

# Table
from todo.models import Task

class TodoView(viewsets.ModelViewSet):
    """ Todo APIS """

    serializer_class = TodoSerializer
    queryset = Task.objects.all()
