from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sosmed(request):
    return render(request,'sosmed.html')
def profil_saya (request) :
    return render(request, 'profil_saya.html')
def index (request) :
    return render(request, 'index.html')
def pengalaman (request) :
    return render(request, 'pengalaman.html')
def pendidikan (request) :
    return render(request, 'pendidikan.html')