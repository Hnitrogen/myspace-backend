from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveDestroyAPIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from django.http import JsonResponse
from rest_framework.decorators import action
from myspace.models.todo import TodoList
from myspace.serializers import TodoListSerializer
from rest_framework import viewsets

class TodoViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


    # def get(self,request):
    #     p = TodoList.objects.all() 
    #     serializer = TodoListSerializer(p,many=True)
    #     return Response(serializer.data)


    @action(detail=False,methods=['get'],url_path='get_simple_todolist')
    def get_simple_todolist(self,request):
        objs = TodoList.objects.all() 
        titles = [{"id": obj.id, "title":obj.title} for obj in objs]
        choices = [y for (x,y) in TodoList.LEVEL_CHOICES]
        return Response({
            "titles": titles , 
            "choices": choices
        })

