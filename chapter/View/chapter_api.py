from rest_framework.viewsets import ModelViewSet 

# Import related serializer and model 


from chapter.Model.chapter_model import ChapterModel 
from chapter.Serializer.chapter_serializer import ChapterSerializer 





class ChapterModelViewSet(ModelViewSet):

    queryset = ChapterModel.objects.all()
    serializer_class = ChapterSerializer