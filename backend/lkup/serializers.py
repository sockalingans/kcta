from rest_framework import serializers
from .models import AssocType, School, AcademyYr, AcademyLvl

class AssocTypeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = AssocType
        fields = '__all__' 


class SchoolSerializer(serializers.ModelSerializer):
    class Meta: 
        model = School
        fields = '__all__' 


class AcademyYrSerializer(serializers.ModelSerializer):
    class Meta: 
        model = AcademyYr
        fields = '__all__' 


class AcademyLvlSerializer(serializers.ModelSerializer):
    class Meta: 
        model = AcademyLvl
        fields = '__all__' 

