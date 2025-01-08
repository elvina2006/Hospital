from .models import *
from modeltranslation.translator import TranslationOptions, register


@register(Profile)
class ProfileTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name')


@register(PatientProfile)
class PatientProfileTranslationOptions(TranslationOptions):
    fields = ('allergies', 'medical_history')


@register(Doctors)
class DoctorsTranslationOptions(TranslationOptions):
    fields = ('qualifications', 'experience_years')


@register(Speciality)
class SpecialityTranslationOptions(TranslationOptions):
    fields = ('speciality',)


@register(Direction_and_Services)
class Direction_and_ServicesTranslationOptions(TranslationOptions):
    fields = ('name', 'picture', 'description', 'doctor')


@register(Name_and_Services)
class Name_and_ServicesTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Department)
class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name', 'dead_id', 'location')


@register(Appointments)
class AppointmentsTranslationOptions(TranslationOptions):
    fields = ('patient_id', 'staff_id', 'status', 'notes', 'date_time')


@register(Prescriptions)
class PrescriptionsTranslationOptions(TranslationOptions):
    fields = ('medication', 'staff_id', 'dosage')


@register(MedicalRecord)
class MedicalRecordTranslationOptions(TranslationOptions):
    fields = ('patient_id', 'doctor_id', 'diagnosis', 'treatment', 'prescribed_medication', 'created_at', 'appointments')


@register(Billing)
class BillingTranslationOptions(TranslationOptions):
    fields = ('patient_id', 'total_amount', 'paid')


@register(Wards)
class WardsTranslationOptions(TranslationOptions):
    fields = ('name', 'ward_type', 'capacity', 'current_occupancy')


@register(Feedbacks)
class FeedbacksTranslationOptions(TranslationOptions):
    fields = ('patient_id', 'doctor_id', 'content')
