from django.db import models

from django.contrib.auth.models import User
from blog.models import Category

Type = (
    ('Doctor','Doctor'),
    ('Patient','Patient')
)

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    type = models.CharField(choices=Type, max_length=50)
    profile_image = models.FileField(upload_to="profile_image/", null=True)
    line1 = models.CharField(max_length=225)
    city = models.CharField(max_length=225)
    state = models.CharField(max_length=225)
    pincode = models.CharField(max_length=225)

class Appoinment(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    specification = models.CharField(max_length=225)
    add_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
