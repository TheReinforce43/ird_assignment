from rest_framework.viewsets import ModelViewSet 

from hadith.Model.hadith_models import hadithModel 

from hadith.Serializer.hadith_serializer import (
    Create_hadithSerializer,
    GetHadithSerializer
)


class HadithViewSet(ModelViewSet):
    queryset = hadithModel.objects.all()

    def get_serializer_class(self):
        if self.action in ['get','retrieve']:
            return GetHadithSerializer
        
        return Create_hadithSerializer