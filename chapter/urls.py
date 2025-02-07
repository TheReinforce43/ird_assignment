from django.urls import path,include 
from rest_framework.routers import DefaultRouter 

from chapter.View.chapter_api import ChapterModelViewSet 


routers =  DefaultRouter()

routers.register(r'',ChapterModelViewSet,basename='chapter')


urlpatterns = [
    path('chapters/',include(routers.urls))
]
