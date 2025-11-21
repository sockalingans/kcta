from rest_framework import viewsets
from .models import Person, Address, PersonAddress, Assoc, Student, Vaguppu, VaguppuStud
from .serializers import PersonSerializer \
                , AddressSerializer \
                , PersonAddressSerializer \
                , AssocSerializer \
                , StudentSerializer \
                , VaguppuSerializer \
                , VaguppuStudSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class PersonAddressViewSet(viewsets.ModelViewSet):
    queryset = PersonAddress.objects.all()
    serializer_class = PersonAddressSerializer


class AssocViewSet(viewsets.ModelViewSet):
    queryset = Assoc.objects.all()
    serializer_class = AssocSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class VaguppuViewSet(viewsets.ModelViewSet):
    queryset = Vaguppu.objects.all()
    serializer_class = VaguppuSerializer


class VaguppuStudViewSet(viewsets.ModelViewSet):
    queryset = VaguppuStud.objects.all()
    serializer_class = VaguppuStudSerializer