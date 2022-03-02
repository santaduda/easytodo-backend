"""
Router to support baisc curd operations
"""
from rest_framework import routers
from apps.todo.views import TodoViewset

router = routers.DefaultRouter()
router.register('todo', TodoViewset, basename="todo")
