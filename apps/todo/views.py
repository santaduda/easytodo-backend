"""
View to manage all Todo related API operations.
"""
#from rest_framework.generics import GenericAPIView
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

class TodoViewset(viewsets.ModelViewSet):
    """
    Get list of all todos created by the user.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
