# Generated by Django 3.2.13 on 2022-08-31 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_doctor', '0002_appoinment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoinment',
            name='add_date',
            field=models.DateField(),
        ),
    ]