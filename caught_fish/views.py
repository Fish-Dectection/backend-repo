from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Caught_fish
from .serializers import CaughtFishSerializer
from django.http import QueryDict

from .tasks import decision
from .models import Fish

from datetime import datetime, timedelta

import requests

# Create your views here.

# def aiResult():
#     mfi = "main_fish_id"
#     mfa = "main_fish_accuracy"
#     s1fi = "sub1_fish_id"
#     s1fa = "sub1_fish_accuracy"
#     s2fi = "sub2_fish_id"
#     s2fa = "sub2_fish_accuracy"

#     return mfi, mfa, s1fi, s1fa, s2fi, s2fa

def discern(fish_info):

    print('판별 함수 test:',fish_info)
    discernVal = fish_info.decode('UTF-8')
    print(type(discernVal))

    # fishId = eval(discernVal)
    # print("id가져오기 test", fishId)

    fishIdsp = discernVal.split(',')
    print("id가져오기2",fishIdsp[0])  #좀더 쉬운 방법이 없을까? 있을거 같은데 파이썬 공부...

    mainFishId = fishIdsp[0].split(':')
    print("정신없어",mainFishId)
    last = mainFishId[1]
    print("mfi",last)
    last= last[0:-1]
    print("mfi",last)
    

    fish_dic = Fish.objects.all()
    print(fish_dic.filter(id=last).values())
    startdate = fish_dic.filter(id=last).values('start_date')
    enddate = fish_dic.filter(id=last).values('end_date')
    print("음", startdate, enddate)

    num1 = startdate
    for i in num1:
        start = i['start_date']
    print("먼스",start)

    num2 = enddate
    for i in num2:
        end = i['end_date']
    print("먼스2",end)

    today = datetime.today()
    print(today)

    sm = start.month
    print("sm",sm)
    lm = end.month
    m = today.month

    sd = start.day
    ld = end.day
    d = today.day
    print("sd",sd)

    if sm<=m and m<=lm:
        if sm==m:
            if d > sd:
                print("불가능")
            else:
                print("가능")
        elif lm==m:
            if d < ld:
                print("불가능")
            else:
                print("가능")
        else :
            print("불가능")
    else :
        print("포획가능")


    return last




class Caught_fish_View(generics.CreateAPIView):
    #queryset = Caught_fish.objects.all()
    serializer_class = CaughtFishSerializer

    def post(self, request):  
        req_serializer =  CaughtFishSerializer(data=request.data)
        
        print(request.data)
        #요청값 데이터 베이스 저장
        req_serializer.is_valid()        
        req_serializer.save()

        #task_id 발급 (Task.py(셀러리)에서 구현)
        task_id = 1

        #셀러리로 전송
        test =  decision(request)
        resultVal = test.content

        #local test        
        # test = requests.post('http://localhost:5001/test/',json={"id": request.data}) 
        # resultVal = test.content
        print(resultVal)

        discernVal = discern(resultVal)
                       
        return Response(task_id, status=200)
       


    def get(self, request):
        task_id = request.GET.get('task_id')
        task = AsyncResult(task_id)
        if not task.ready():
            return Response({"WARNING"})
        data = task.result
        return Response(data, status=200)

