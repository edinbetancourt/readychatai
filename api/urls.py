""" restapi URL Configuration """

from django.urls import path, include
from rest_framework import routers

from api.views import todo

router = routers.DefaultRouter()
router.register(r'test/v1/todo', todo.TodoView, basename='doto')

urlpatterns = [

    # Django Rest links
    path('', include(router.urls)),
]
