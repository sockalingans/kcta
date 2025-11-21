from rest_framework import serializers
from .models import Person, Address, PersonAddress, Assoc, Student, Vaguppu, VaguppuStud

class PersonSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Person
        fields = '__all__' 


class AddressSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Address
        fields = '__all__' 


class PersonAddressSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PersonAddress
        fields = '__all__' 


class AssocSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Assoc
        fields = '__all__' 


class StudentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Student
        fields = '__all__' 


class VaguppuSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Vaguppu
        fields = '__all__' 


class VaguppuStudSerializer(serializers.ModelSerializer):
    class Meta: 
        model = VaguppuStud
        fields = '__all__' 
