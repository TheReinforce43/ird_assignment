from django.db import models
import uuid 

from section.Model.section_model import SectionModel 
from chapter.Model.chapter_model import ChapterModel 


class hadithModel(models.Model):

    uuid =  models.UUIDField(default = uuid.uuid4, unique=True,editable=False)

    description = models.TextField()
    chapter = models.ForeignKey(ChapterModel, on_delete=models.CASCADE,related_name='hadith_chapter',null=True)
    section = models.ForeignKey(SectionModel, on_delete=models.CASCADE,related_name='hadith_section',null=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Hadith ID : {self.id}' 

