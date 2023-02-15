from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Fish 
from .serializers import FishSerializer
class FishDetailView(APIView):
    def get(self, request, fish_id, format=None):
        try:
            fish = Fish.objects.get(id=fish_id)
        except Fish.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        fish_serializer = FishSerializer(fish)
        return Response({"fish": fish_serializer.data})
    


