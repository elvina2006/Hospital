# Generated by Django 5.1.4 on 2025-01-06 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0003_patientprofile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='doctor_image',
            field=models.ImageField(default=1, upload_to='doctor_images/'),
            preserve_default=False,
        ),
    ]
