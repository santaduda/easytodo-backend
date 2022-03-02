"""
Model definition for Todo app
"""

from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    """
    Stores a single todo entry, related to :model:`auth.User`.
    """
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)
