import uuid

from django.utils import timezone 
from django.db import models

# Create your models here.

class Task(models.Model):
    """ Task table """
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
