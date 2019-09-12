from django.shortcuts import render
from .models import Service


# Create your views here.

def service(request):
	service = Service.objects.all()
	return render(request,'services/services.html', {'service':service})