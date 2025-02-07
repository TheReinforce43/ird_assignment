from django.urls import path ,include 
from rest_framework.routers import DefaultRouter
from section.View.section_api import SectionViewSet
router = DefaultRouter() 


router.register(r'',SectionViewSet)



urlpatterns = [
    path('section/',include(router.urls)),
]
