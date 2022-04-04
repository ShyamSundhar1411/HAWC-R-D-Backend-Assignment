from django.urls import path,include
from . import views

urlpatterns = [
    #Hospitals
    path("view/hospitals",views.viewhospitals,name = "view_all_hospitals"),
    path("add/hospital",views.AddHospitalView.as_view(),name = "add_hospital"),
    path("update/<int:pk>/<slug:slug>/hospital",views.UpdateHospitalView.as_view(),name = "update_hospital_details"),
    path("delete/<int:pk>/<slug:slug>/hospital/profile",views.deletehospital,name = "delete_hospital_profile"),
    #Doctors
    path("view/doctors",views.viewdoctors,name = "view_all_doctors"),
    path("add/doctor",views.AddDoctorView.as_view(),name = "add_doctor"),
    path("update/<int:pk>/<slug:slug>/doctor",views.UpdateDoctorView.as_view(),name = "update_doctor_details"),
    path("delete/<int:pk>/<slug:slug>/doctor/profile",views.deletedoctor,name = "delete_doctor_profile"),
    path("view/<int:pk>/doctors/<slug:slug>/related/hospital",views.doctorsrelatedtohospital,name = "view_doctors_realted_to_hospital"),
]