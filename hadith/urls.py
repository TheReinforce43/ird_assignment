from django.urls import path ,include 

from rest_framework.routers import DefaultRouter 
from hadith.View.hadith_api import HadithViewSet 

routers = DefaultRouter()

routers.register(r'hadith', HadithViewSet, basename='hadith')






urlpatterns = [
    path('',include(routers.urls)),
]
