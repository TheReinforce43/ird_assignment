from rest_framework import serializers 

# import related serializer and model 
from section.Model.section_model import SectionModel 
from chapter.Serializer.chapter_serializer import ChapterSerializer 



class CreateSectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SectionModel
        fields = ('id', 'chapter', 'section_name', 'created_at', 'updated_at')



class GetSectionSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer()

    class Meta:
        model = SectionModel
        fields = ('id', 'chapter', 'section_name', 'created_at', 'updated_at')


