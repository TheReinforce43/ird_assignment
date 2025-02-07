from rest_framework.viewsets import ModelViewSet 

from section.Model.section_model import SectionModel 
from section.Serializer.section_serializer import (
    CreateSectionSerializer,
    GetSectionSerializer
)



class SectionViewSet(ModelViewSet):

    queryset = SectionModel.objects.all()

    def get_serializer_class(self):
        if self.action in ['list','retrieve'] :
            return GetSectionSerializer
        
        return CreateSectionSerializer