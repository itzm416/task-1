from django.contrib import admin
from patient_doctor.models import Appoinment, Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username','profile_image','first_name','last_name','email','type','line1','city','state','pincode')

@admin.register(Appoinment)
class AppoinmentAdmin(admin.ModelAdmin):
    list_display = ('username','specification','add_date')
