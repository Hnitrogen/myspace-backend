from myspace.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

class UserList(APIView):
    def get(self,request,user_id):
        p = User.objects.get(id=user_id) 
        serializer = UserSerializer(p) 
        return Response(serializer.data) 