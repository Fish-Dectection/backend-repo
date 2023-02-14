# from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Fish, FishImage
from .serializers import FishSerializer, FishImageSerializer

'''class FishViewSet(viewsets.ModelViewSet):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer

    def retrieve(self, request, pk=None):
        try:
            fish = Fish.objects.get(id=pk)
        except Fish.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = FishSerializer(fish)
        return Response(serializer.data)'''

class FishDetailView(APIView):
    def get(self, request, fish_id, format=None):
        try:
            fish = Fish.objects.get(id=fish_id)
        except Fish.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = FishSerializer(fish)
        return Response(serializer.data)
