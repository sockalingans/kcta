from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
from lkup.models import School, AssocType, AcademyLvl, AcademyYr


class Person(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('U', 'Unknown'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='Unknown')
    dob = models.DateField()
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s, %s" % (self.lastname, self.firstname)


class Address(models.Model):
    street=models.CharField(max_length=255)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=50)
    zipcode=models.CharField(max_length=5
            , validators=[RegexValidator('^[0-9]{5}$'
                                     , message='Invalid postal code'
                                     , code="Invalid zipcode")],
    )
    country=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s, %s, %s %s" % (self.street, self.city, self.state, self.zipcode)


class PersonAddress(models.Model):
    person=models.ForeignKey(Person, on_delete=models.CASCADE)
    address=models.ForeignKey(Address, on_delete=models.CASCADE)
    eff_from = models.DateField()
    eff_thru = models.DateField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.person.lastname, self.address.city)


class Assoc(models.Model):
    person_1=models.ForeignKey(Person, related_name='person_pri', on_delete=models.CASCADE)
    assoc_type=models.ForeignKey(AssocType, on_delete=models.CASCADE)
    person_2=models.ForeignKey(Person, related_name='person_sec', on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s of %s" % (self.person_1.firstname, self.assoc_type.name, self.person_2.firstname)


class Student(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    GRADE_CHOICES = [
        ('K1', 'Kindergarten 1'),
        ('K2', 'Kindergarten 2'),
        ('01', '1st Grade'),
        ('02', '2nd Grade'),        
        ('03', '3rd Grade'),    
        ('04', '4th Grade'),        
        ('05', '5th Grade'),        
        ('06', '6th Grade'),        
        ('07', '7th Grade'),        
        ('08', '8th Grade'),        
        ('09', '9th Grade'),        
        ('10', '10th Grade'),        
        ('11', '11th Grade'),        
        ('12', '12th Grade'),        
    ]
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s @ %s" % \
            (self.person.lastname, self.get_grade_display(), self.school.name)


class Vaguppu(models.Model):
    teacher= models.ForeignKey(Person, related_name='teacher', on_delete=models.DO_NOTHING)
    delegate = models.ForeignKey(Person, related_name='delegate', blank=True, null=True, on_delete=models.DO_NOTHING)
    academyyr = models.ForeignKey(AcademyYr, on_delete=models.DO_NOTHING)
    academylvl = models.ForeignKey(AcademyLvl, on_delete=models.DO_NOTHING)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Teacher: %s for %s (Level: %s)" % \
            (self.teacher.firstname, self.academyyr, self.academylvl)

    class Meta:
        verbose_name = "vaguppu"
        verbose_name_plural = "vaguppugal"


class VaguppuStud(models.Model):
    vaguppu = models.ForeignKey(Vaguppu, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s (Student) of %s" % \
            (self.student.person.firstname, self.vaguppu)

    class Meta:
        verbose_name = "vaguppu_maanavar"
        verbose_name_plural = "vaguppu_maanavargal"
