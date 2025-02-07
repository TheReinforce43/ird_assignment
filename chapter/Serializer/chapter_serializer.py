from rest_framework import serializers 

from chapter.Model.chapter_model import ChapterModel 




class ChapterSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChapterModel
        fields = '__all__'