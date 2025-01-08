from .views import *
from rest_framework import routers
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'profile', ProfileViewSet, basename='profiles')
router.register(r'patient-list', PatientProfileListViewSet, basename='patients_list')
router.register(r'patient-detail', PatientProfileDetailViewSet, basename='patients_detail')
router.register(r'doctors', DoctorsListViewSet, basename='doctors_list')
router.register(r'doctors-detail', DoctorsDetailViewSet, basename='doctors_detail')
router.register(r'cantact-info', CantactInfoViewSet, basename='cantact_info')
router.register(r'speciality', SpecialityViewSet, basename='speciality')
router.register(r'department', DepartmentViewSet, basename='departments')
router.register(r'appointment', AppointmentsViewSet, basename='appointments')
router.register(r'medical_record', MedicalRecordViewSet, basename='medical_record')
router.register(r'prescription', PrescriptionsViewSet, basename='prescriptions')
router.register(r'billing', BillingViewSet, basename='billing')
router.register(r'ward', WardsViewSet, basename='wards')
router.register(r'feedback', FeedbacksViewSet, basename='feedbacks')


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('', include(router.urls)),
    ]
