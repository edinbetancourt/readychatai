from rest_framework import serializers

from todo.models import Task

class TodoSerializer(serializers.ModelSerializer):
    """ Serializer for TodoView """

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['id', 'created']
