from django.contrib import admin
from .models import Person \
            , Address \
            , PersonAddress \
            , Assoc \
            , Student \
            , Vaguppu \
            , VaguppuStud

# Register your models here.
admin.site.register(Person)
admin.site.register(Address)
admin.site.register(PersonAddress)
admin.site.register(Assoc)
admin.site.register(Student)
admin.site.register(Vaguppu)
admin.site.register(VaguppuStud)