from rest_framework import viewsets
from .models import AssocType, School, AcademyYr, AcademyLvl
from .serializers import AssocTypeSerializer, SchoolSerializer, AcademyYrSerializer, AcademyLvlSerializer

class AssocTypeViewSet(viewsets.ModelViewSet):
    queryset = AssocType.objects.all()
    serializer_class = AssocTypeSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class AcademyYrViewSet(viewsets.ModelViewSet):
    queryset = AcademyYr.objects.all()
    serializer_class = AcademyYrSerializer


class AcademyLvlViewSet(viewsets.ModelViewSet):
    queryset = AcademyLvl.objects.all()
    serializer_class = AcademyLvlSerializer
