from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

from myspace.models.tutorial.project import Project
from myspace.serializers import ProjectSerializer

class ProjectList(APIView):
    def get(self,request):
        p = Project.objects.all() 
        serializer = ProjectSerializer(p,many=True) 
        return Response(serializer.data)
