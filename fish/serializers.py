from rest_framework import serializers
from .models import Fish, FishImage #CaughtFish

class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = (
            'fish_name', 
            'scientific_name', 
            'start_date', 
            'end_date', 
            'prohibition_length', 
            'prohibition_region', 
            'description')

    def create(self, validated_data):
        fish = Fish.objects.create(**validated_data)
        return fish

    def update(self, instance, validated_data):
        instance.fish_name = validated_data.get('fish_name', instance.fish_name)
        instance.scientific_name = validated_data.get('scientific_name', instance.scientific_name)
        instance.prohibition_period = validated_data.get('prohibition_period2', instance.prohibition_period)
        instance.prohibition_length = validated_data.get('prohibition_length', instance.prohibition_length)
        instance.prohibition_region = validated_data.get('prohibition_region', instance.prohibition_region)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

    def delete(self, instance):
        instance.is_deleted = True
        instance.save()


class FishImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishImage
        fields = ('fish_id', 'image_url')
    
    def create(self, validated_data):
        fish = FishImage.objects.create(**validated_data)
        return fish

    def update(self, instance, validated_data):
        instance.image_url = validated_data.get('image_url', instance.description)
        instance.save()
        return instance

    def delete(self, instance):
        instance.is_deleted = True
        instance.save()

'''class CaughtFishSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaughtFish
        fields = ('fish_length', 'user_region', 'image_url', 'main_fish_id', 'main_fish_accurancy', 'sub1_fish_id', 'sub1_fish_accuracy', 'sub2_fish_id', 'sub2_fish_accuracy')'''

