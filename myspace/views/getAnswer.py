from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import JsonResponse
from myspace.models.Timer import Timer , Answer
from myspace.serializers import TimerSerializer , AnswerSerializer
from django.http import HttpResponse

import pytz
import json
import datetime

@csrf_exempt

def setTimer(request): 
    now = datetime.datetime.now()
    later = now + datetime.timedelta(seconds=15) 

    p = Timer.objects.get(tid=0) 
    p.TimeStamp = later 
    p.save() 
    
    Answers = Answer.objects.all() 
    for item in Answers: 
        item.delete()

    return JsonResponse({'result':later}) 

class getAnswer(APIView):
    permission_classes = ([IsAuthenticated])
    # authentication_classes = [JWTAuthentication]

    def get(self,request):
        # permission_classes = ([IsAuthenticated])    # 鉴权
        authentication_classes = [JWTAuthentication]
        p = Answer.objects.all()
        serializer = AnswerSerializer(p,many=True) 
        return Response(serializer.data)
    
    def post(self,request):
        # 我觉得前端记录时间比较公平hhh
        if request.method == 'POST': 

            id = request.POST.get('id')
            time_string = request.POST.get('time')
            t1 , t2 , t3 , t4, t5 , t6 , t7 = time_string.split()
        # Tue  May  23 2023 22:34:09 GMT+0800 (中国标准时间)
        
            hour , minute , second = t5.split(':') 
            time_format = datetime.datetime(2023,5,int(t3),int(hour),int(minute),int(second)) 

            Answer.objects.create(user_id=id,TimeStamp=time_format)
            return JsonResponse({'result':'post_success'})


class getTimeStamp(APIView):
    def get(self,request):
        p = Timer.objects.all()
        serializer = TimerSerializer(p,many=True) 
        return Response(serializer.data)
