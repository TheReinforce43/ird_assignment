from django.contrib import admin

# Register your models here.
from hadith.Model.hadith_models import hadithModel 

admin.site.register(hadithModel) 