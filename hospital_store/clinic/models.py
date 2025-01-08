from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField


class Profile(AbstractUser):
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='picture/')
    ROLE_CHOICES = [
        ('администратор', 'администратор'),
        ('врач', 'врач'),
        ('пациент', 'пациент'),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='пациент')
    groups = models.ManyToManyField(Group, related_name='profile_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='profile_permissions', blank=True)
    address = models.TextField()
    date_of_birth = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class PatientProfile(models.Model):
    name = models.CharField(max_length=32)
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='patientProfile')
    emergency_contact = models.CharField(max_length=20, null=True, blank=True)
    blood_type = models.CharField(max_length=5, null=True, blank=True)
    allergies = models.TextField(null=True,  blank=True)
    medical_history = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.emergency_contact}'


class Doctors(models.Model):
    doctor_name = models.CharField(max_length=222)
    doctor_image = models.ImageField(upload_to='doctor_images/')
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='doctor_profile')
    shift_start = models.TimeField(null=True, blank=True)
    shift_end = models.TimeField(null=True, blank=True)
    qualifications = models.CharField(max_length=15)
    experience_years = models.CharField(max_length=5)
    WEEKS_DAY = [
        ('monday', 'monday'),
        ('tuesday', 'tuesday'),
        ('wednesday', 'wednesday'),
        ('thursday', 'thursday'),
        ('friday', 'friday'),
        ('saturday', 'saturday'),
        ('sunday', 'sunday'),
    ]
    working_days = MultiSelectField(max_length=32, choices=WEEKS_DAY, max_choices=3)

    def __str__(self):
        return f'{self.qualifications}, {self.experience_years},{self.doctor_name}'


class ContactInfo(models.Model):
    hospital = models.ForeignKey(Doctors, on_delete=models.CASCADE, related_name='hospitals')

    phone_number = PhoneNumberField(region='KG', null=True, blank=True)


class Speciality(models.Model):
    speciality = models.ForeignKey(Doctors, on_delete=models.CASCADE, related_name='speciality')

    def __str__(self):
        return f'{self.speciality}'


class Direction_and_Services(models.Model):
    name = models.CharField(max_length=250)
    picture = models.ImageField(upload_to='pictures/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    doctor = models.ManyToManyField(Doctors)

    def __str__(self):
        return self.name


class Name_and_Services(models.Model):
    name = models.ForeignKey(Direction_and_Services, on_delete=models.CASCADE, related_name='service_name')
    description = models.TextField()

    def __str__(self):
        return f'{self.name}, {self.description}'


class Department(models.Model):
    name = models.CharField(max_length=20)
    dead_id = models.ForeignKey(Doctors, on_delete=models.CASCADE, related_name='dead_id')
    location = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return f'{self.name}'


class Appointments(models.Model):
    patient_id = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='patient_id')
    staff_id = models.ForeignKey(Doctors, on_delete=models.CASCADE, related_name='staff_id')
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15)
    notes = models.TextField()

    def __str__(self):
        return f'{self.status}'


class MedicalRecord(models.Model):
    patient_id = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='medicalrecord')
    doctor_id = models.ForeignKey(Doctors, on_delete=models.CASCADE, related_name='doctor_id')
    diagnosis = models.CharField(max_length=45)
    treatment = models.CharField(max_length=40)
    prescribed_medication = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    appointments = models.ForeignKey(Appointments, on_delete=models.CASCADE, related_name='Appointments')

    def __str__(self):
        return f'{self.diagnosis}, {self.treatment}'


class Prescriptions(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, related_name='medical_records')
    patient_id = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='prescriptions')
    staff_id = models.ForeignKey(Doctors, on_delete=models.CASCADE, related_name='doctor')
    medication = models.CharField(max_length=15)
    dosage = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.medication}, {self.dosage}'


class Billing(models.Model):
    patient_id = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='billing')
    total_amount = models.PositiveIntegerField(null=True, blank=True)
    paid = models.BooleanField(default=False)
    issued_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.patient_id}, {self.issued_date}'


class Wards(models.Model):
    name = models.CharField(max_length=20, unique=True)
    ward_type = models.CharField(max_length=32)
    capacity = models.CharField(max_length=32)
    current_occupancy = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.name}, {self.ward_type}'


class Feedbacks(models.Model):
    doctor_id = models.ForeignKey(Doctors, on_delete=models.CASCADE, related_name='feedbacks')
    patient_id = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='patient')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor_id}, {self.patient_id}'
