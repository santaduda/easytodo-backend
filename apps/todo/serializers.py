'''
Todo app Serializer
'''
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    '''
    To serialize all todo model data
    '''
    class Meta:
        model = Todo
        fields = ['title', 'author']
