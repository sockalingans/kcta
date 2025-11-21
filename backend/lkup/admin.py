from django.contrib import admin
from .models import AssocType, School, AcademyYr, AcademyLvl

# Register your models here.
admin.site.register(AssocType)
admin.site.register(School)
admin.site.register(AcademyYr)
admin.site.register(AcademyLvl)