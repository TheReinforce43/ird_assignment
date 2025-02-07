from django.db import models 

from chapter.Model.chapter_model import ChapterModel 

import uuid


class SectionModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4,unique=True,editable=False )
    chapter= models.ForeignKey(ChapterModel, related_name = 'sections_chapter',on_delete=models.CASCADE,db_index=True)

    section_name = models.CharField(max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'section name : {self.section_name}'

