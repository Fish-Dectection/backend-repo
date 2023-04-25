from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Caught_fish, Fish
from .serializers import CaughtFishSerializer
from django.http import QueryDict

# from .tasks import decision
# from celery.result import AsyncResult

from datetime import datetime, timedelta

import requests
from django.http import HttpResponse
import json

from django.http import JsonResponse

def region_cp(fish_info, request):
    E_fish_name = fish_info['name']
    fish_dic = Fish.objects.all()

    location = fish_dic.filter(E_fish_name=E_fish_name).values('prohibition_region')

    prohibit_r = []
    for i in location:
        prohibit_r.append(i['prohibition_region'])
    # print("지역스", prohibit_r)

    user_location = request.POST['location']

    if user_location in prohibit_r:
        region_return = "%s 포획 가능" % user_location
    else:
        region_return = "%s 포획 불가능" % user_location
    
    return region_return

def length_cp(fish_info, request):
    E_fish_name = fish_info['name']
    fish_dic = Fish.objects.all()

    len = fish_dic.filter(E_fish_name=E_fish_name).values('prohibition_length')

    for i in len:
        length = i['prohibition_length']
    
    user_length = float(request.POST['length'])

    if user_length >= length:
        length_return = "금지체장 해당됨"
    else:
        length_return = "금지체장에 해당안됨"

    return length_return

def phdate_cp(fish_info, request):
    E_fish_name = fish_info['name']
    fish_dic = Fish.objects.all()

    startdate = fish_dic.filter(E_fish_name=E_fish_name).values('start_date')
    enddate = fish_dic.filter(E_fish_name=E_fish_name).values('end_date')

    for i in startdate:
        start = i['start_date']

    for i in enddate:
        end = i['end_date']

    today = datetime.today()

    sm = start.month
    lm = end.month
    tm = today.month

    sd = start.day
    ld = end.day
    d = today.day

    if sm<=tm and tm<=lm:
        if sm==tm:
            if d > sd:
                returnVal = "금어기"
            else:
                returnVal = "금어기 해당안됨"
        elif lm==tm:
            if d < ld:
                returnVal = "금어기"
            else:
                returnVal = "금어기 해당안됨"
        else :
            returnVal = "금어기"
    else :
        returnVal = "포획가능"

    return returnVal

# discern = DB에 저장된 금어기 정보 불러와서 딥러닝 판별결과랑 비교해서 최종 포획 가능 여부 판별하는 함수.
# fish_ifo = 사용자 입력(위치, 길이, 이미지)
def discern(fish_info, request): 
    E_fish_name = fish_info['name']
    print('ff:', E_fish_name)

    confidence = fish_info["confidence"]

    fish_dic = Fish.objects.all()
    
    return_rg = region_cp(fish_info, request)
    return_lg = length_cp(fish_info, request)
    return_pd = phdate_cp(fish_info, request)

    fish_name = fish_dic.get(E_fish_name=E_fish_name).fish_name
    return_sd = fish_dic.get(E_fish_name=E_fish_name).start_date
    return_ed = fish_dic.get(E_fish_name=E_fish_name).end_date
    return_region = fish_dic.get(E_fish_name=E_fish_name).prohibition_region
    return_length = fish_dic.get(E_fish_name=E_fish_name).prohibition_length

    return fish_name, confidence, return_sd, return_ed, return_length, return_region, return_pd, return_lg, return_rg

class Caught_fish_View(generics.CreateAPIView):
    serializer_class = CaughtFishSerializer

    def post(self, request):  
        req_serializer =  CaughtFishSerializer(data=request.data)
        print(request.data)

        # 이미지 파일 가져오기
        image_file = request.FILES.get('image')

        # flask 서버로 이미지 파일 전송
        if image_file:
            url = 'http://127.0.0.1:5003/v1/object-detection/fishmo'
            files = {'image': image_file}
            response = requests.post(url, files = files)
            resultVal = response.content
            print(resultVal)

        else:
            resultVal = None

        # ai서버로부터 받은 결과값을 딕셔너리로 반환
        result_dict = json.loads(resultVal)

        # 정확도, 어류 이름 딕셔너리로 반환
        resultVal = {"confidence": result_dict[0]['confidence'], "name": result_dict[0]['name']}

        discernVal = discern(resultVal, request)
        
        return JsonResponse({"response": "{0}".format(discernVal)},status=200)

