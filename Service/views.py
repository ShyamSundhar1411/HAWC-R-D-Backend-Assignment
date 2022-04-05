from .models import Hospital,Doctor
from .filters import HospitalFilter,DoctorFilter
from django import forms
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy,reverse
from django.db.models import Count


# Create your views here.
#Class Based Views
#Hospitals
class AddHospitalView(SuccessMessageMixin,generic.CreateView):
    model = Hospital
    fields = ['Hospital_Name','Hospital_Code','Location']
    template_name = "Service/Hospital/AddHospital.html"
    success_url = reverse_lazy("view_all_hospitals")
    success_message = "Added Hospital successfully"
    def form_valid(self,form):
        return super().form_valid(form)
class UpdateHospitalView(generic.UpdateView):
    model = Hospital
    fields = ['Hospital_Name','Hospital_Code','Location']
    slug_field = Hospital.slug
    template_name = "Service/Hospital/UpdateHospitalDetails.html"
    def get_success_url(self):
        pk = self.kwargs["pk"]
        slug = self.kwargs["slug"]
        messages.success(self.request,'Updated Successfully')
        return reverse("update_hospital_details", kwargs={"pk": pk,'slug':slug})
#Doctors
class AddDoctorView(SuccessMessageMixin,generic.CreateView):
    model = Doctor
    fields = ["Doctor_Name","Doctor_Id","Profile_Picture","Date_of_Joining","Qualification","Specialization","Hospital"]   
    template_name = "Service/Doctor/AddDoctor.html"
    success_url = reverse_lazy("view_all_doctors")
    success_message = "Added Doctor successfully"
    def get_form(self, form_class=None):
        form = super(AddDoctorView, self).get_form(form_class)
        form.fields['Date_of_Joining'].widget = forms.DateInput(format='%d/%m/%Y')
        return form
    def form_valid(self,form):
        return super().form_valid(form)
class UpdateDoctorView(generic.UpdateView):
    model = Doctor
    fields = ["Doctor_Name","Doctor_Id","Profile_Picture","Date_of_Joining","Qualification","Specialization","Hospital"] 
    slug_field = Doctor.slug
    template_name = "Service/Doctor/UpdateDoctorDetails.html"
    def get_success_url(self):
        pk = self.kwargs["pk"]
        slug = self.kwargs["slug"]
        messages.success(self.request,'Updated Successfully')
        return reverse("update_doctor_details", kwargs={"pk": pk,'slug':slug})
    
#Function Based Views
def home(request):
    return render(request,"Service/home.html")
def viewhospitals(request):
    hospital_list = Hospital.objects.order_by("Hospital_Code").all()
    hospital_filter = HospitalFilter(request.GET, queryset=hospital_list)
    return render(request, 'Service/Hospital/viewhospitals.html', {'Hospitals': hospital_filter,})
def viewdoctors(request):
    doctors = Doctor.objects.prefetch_related("Hospital").order_by("-Date_of_Joining").all()
    doctor_filter = DoctorFilter(request.GET)
    return render(request,"Service/Doctor/viewdoctors.html",{"Doctors":doctor_filter})
def deletedoctor(request,pk,slug):
    Doctor_Profile = Doctor.objects.prefetch_related("Hospital").get(id = pk,slug = slug)
    if request.method == "POST":
        Doctor_Profile.delete()
        messages.success(request,"Deleted Doctor Profile successfully")
        return redirect("view_all_doctors")
def deletehospital(request,pk,slug):
    Hospital_Profile = Hospital.objects.get(id = pk,slug = slug)
    if request.method == "POST":
        Hospital_Profile.delete()
        messages.success(request,"Deleted Hospital Profile successfully")
        return redirect("view_all_hospitals")
def doctorsrelatedtohospital(request,pk,slug):
    Hospital_Profile = Hospital.objects.get(id = pk,slug = slug)
    doctors = Doctor.objects.prefetch_related("Hospital").filter(Hospital = Hospital_Profile).order_by("-Date_of_Joining")
    return render(request,"Service/relateddoctors.html",{"Doctors":doctors,"Hospital":Hospital_Profile})
    