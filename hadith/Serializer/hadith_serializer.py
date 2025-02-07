from rest_framework import serializers 

# import related serializer and model classes 

from hadith.Model.hadith_models import hadithModel 

from chapter.Serializer.chapter_serializer import ChapterSerializer
from section.Serializer.section_serializer import  GetSectionSerializer 


class Create_hadithSerializer(serializers.ModelSerializer):

    class Meta:
        model = hadithModel
        fields = '__all__'



class GetHadithSerializer(serializers.ModelSerializer):

    chapter = ChapterSerializer()
    section = GetSectionSerializer(many=True)

    class Meta:
        model = hadithModel
        fields = '__all__'
