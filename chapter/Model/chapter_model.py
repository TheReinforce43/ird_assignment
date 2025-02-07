from django.db import models 
import uuid

class ChapterModel(models.Model):
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    chapter_name  = models.CharField(max_length=100,unique=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'chapter name : {self.chapter_name}'