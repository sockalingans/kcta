from django.db import models
from datetime import date

# Create your models here.
class AssocType(models.Model):
    name=models.CharField(max_length=100, unique=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class School(models.Model):
    name=models.CharField(max_length=255, unique=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AcademyYr(models.Model):
    eff_from =  models.DateField()
    eff_thru = models.DateField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s thru %s" % (self.eff_from.strftime("%b %d, %Y"), self.eff_thru.strftime("%b %d, %Y"))


class AcademyLvl(models.Model):
    name=models.CharField(max_length=100, unique=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name