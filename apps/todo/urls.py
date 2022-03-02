"""
Todo app URL Configuration
"""
from django.urls import path
from .views import TodoViewset

urlpatterns = [
    path('', TodoViewset.as_view(), name='todo'),
]
