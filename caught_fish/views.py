from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Caught_fish
from .serializers import CaughtFishSerializer
from django.http import QueryDict


# Create your views here.

def aiResult():
    mfi = "main_fish_id"
    mfa = "main_fish_accuracy"
    s1fi = "sub1_fish_id"
    s1fa = "sub1_fish_accuracy"
    s2fi = "sub2_fish_id"
    s2fa = "sub2_fish_accuracy"

    return mfi, mfa, s1fi, s1fa, s2fi, s2fa

class Caught_fish_View(generics.CreateAPIView):
    #queryset = Caught_fish.objects.all()
    serializer_class = CaughtFishSerializer

    def post(self, request):  
        req_serializer =  CaughtFishSerializer(data=request.data)
        
        print(request)
        #요청값 데이터 베이스 저장
        req_serializer.is_valid()        
        req_serializer.save()

        #task_id 발급 (Task.py(셀러리)에서 구현)
        task_id = 1

        #셀러리로 전송                
                       
        return Response(task_id, status=200)
       


    def get(self, request):
        task_id = request.GET.get('task_id')
        task = AsyncResult(task_id)
        if not task.ready():
            return Response({"WARNING"})
        data = task.result
        return Response(data, status=200)

