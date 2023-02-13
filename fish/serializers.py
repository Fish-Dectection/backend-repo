from rest_framework import serializers
from .models import Fish, FishImage, CaughtFish

class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = ('fish_name', 'scientific_name', 'prohibition_period', 'prohibition_length', 'prohibition_region', 'description')

class FishImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishImage
        fields = ('fish_id', 'image_url')

class CaughtFishSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaughtFish
        fields = ('fish_length', 'user_region', 'image_url', 'main_fish_id', 'main_fish_accurancy', 'sub1_fish_id', 'sub1_fish_accuracy', 'sub2_fish_id', 'sub2_fish_accuracy')

