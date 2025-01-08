from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'password',  'age',
                  'phone_number', ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Profile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class PatientProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = ['name', 'emergency_contact']


class PatientProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = ['name', 'user', 'blood_type', 'emergency_contact', 'allergies', 'medical_history']


class DoctorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ['doctor_name', 'doctor_image']


class DoctorsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ['doctor_name', 'doctor_image', 'user', 'shift_start', 'shift_end', 'qualifications',
                  'experience_years', 'working_days',]


class CantactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = '__all__'


class Direction_and_ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction_and_Services
        fields = '__all__'


class Name_and_ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name_and_Services
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = '__all__'


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'


class PrescriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescriptions
        fields = '__all__'


class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = '__all__'


class WardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wards
        fields = '__all__'


class FeedbacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedbacks
        fields = '__all__'

