from django.shortcuts import render, redirect
from django.http import Http404
from .models import Car, Pincode
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def request_a_service(request):
    return render(request, 'request_a_service.html' )

def we_come_to_you(request):
    return render(request, 'we_come_to_you.html' )

def we_warranty_our_services(request):
    return render(request, 'we_warranty_our_services.html' )

def get_maintenance_reminders(request):
    return render(request, 'get_maintenance_reminders.html' )

def services(request):
    return render(request, 'services.html')

def book(request):
    return render(request, 'book.html')