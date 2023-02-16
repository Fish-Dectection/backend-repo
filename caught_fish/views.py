from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Caught_fish
from .serializers import CaughtFishResponseSerializer, CaughtFishRequestSerializer
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
    serializer_class = CaughtFishResponseSerializer

    def post(self, request):  
        req_serializer =  CaughtFishResponseSerializer(data=request.data)
        
        print(request)
        #요청값 데이터 베이스 저장
        req_serializer.is_valid()        
        req_serializer.save()
                
        #ai 결과값 받는 임시 함수
        mfi, mfa, s1fi, s1fa, s2fi ,s2fa = aiResult()         
        print(mfi, mfa, s1fi, s1fa, s2fi ,s2fa)

        # responseVal = QueryDict('main_fish_id="{0}"&main_fish_accuracy={1}&sub1_fish_id={2}&sub1_fish_accuracy={3}&sub2_fish_id={4}&sub2_fish_accuracy={5}'.format(mfi, mfa, s1fi, s1fa, s2fi, s2fa))
        # #responseVal = QueryDict.fromkeys(['main_fish_id','main_fish_accuracy','sub1_fish_id','sub1_fish_accuracy','sub2_fish_id','sub2_fish_accuracy'],value={'main_fish_id':mfi})
        # print(responseVal)

        # req_serializer.is_valid()
        
        req_serializer = CaughtFishResponseSerializer(self, data={'main_fish_id': 'test'},partial=True)

        req_serializer.is_valid()        
        req_serializer.save()
        

        return Response({"main_fish_id": mfi, "main_fish_accuracy": mfa, "sub1_fish_id": s1fa, "sub1_fish_accuracy": s1fa, "sub2_fish_id": s2fi, "sub2_fish_accuracy": s2fa})


    def caught_create(self, serializer):
        caught = Caught_fish.objects.get()