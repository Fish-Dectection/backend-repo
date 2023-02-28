from django.urls import path
from .views import *

urlpatterns = [
    path('fish/<int:fish_id>', FishDetailView.as_view(), name='fish'),
    path('fish/<int:fish_id>/image', FishImageView.as_view(), name='fish-image'),
]
