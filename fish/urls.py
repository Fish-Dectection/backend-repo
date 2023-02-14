from django.urls import path
from .views import FishDetailView

urlpatterns = [
    path('fish/<int:fish_id>/', FishDetailView.as_view(), name='fish'),
]
