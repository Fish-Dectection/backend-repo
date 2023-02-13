from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FishDetailView

router = DefaultRouter()
router.register(r'fish', FishDetailView, basename='fish')

urlpatterns = [
    path('', include(router.urls))
]
