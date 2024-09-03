from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from myspace.models.post import Post , PostComment
from myspace.serializers import PostSerializer , PostCommentSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator 
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view

import os 
import subprocess

# 远程执行shell命令，有且只能以wakeonlan开头，并只支持两种参数
@api_view(['GET'])
def turn_on(request):
    mac_address = request.GET.get('mac_address','')
    ip_address = request.GET.get('ip_address','')

    command = "wakeonlan "
    if mac_address:
        command += mac_address
    else:
        command += ip_address
    

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    decode_output = output.decode('utf-8')

    
    response_data = {
        'command': command,
        'output': decode_output.split('\n'),
        'error': error.decode('utf-8')
    }

    return Response(response_data)