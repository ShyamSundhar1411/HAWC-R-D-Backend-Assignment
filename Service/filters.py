import django_filters
from django_filters import DateRangeFilter
from .models import Hospital,Doctor

class HospitalFilter(django_filters.FilterSet):
    class Meta:
        model = Hospital
        fields = ['Hospital_Name','Hospital_Code','Location']
class DoctorFilter(django_filters.FilterSet):
    Date_of_Joining = DateRangeFilter(label ='Date of Joining')
    class Meta:
        model = Doctor
        fields = ['Doctor_Name','Hospital','Qualification','Date_of_Joining','Specialization']