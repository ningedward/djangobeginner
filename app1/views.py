from django.shortcuts import render,redirect
from django.urls import reverse

from django.http import HttpResponse

def test1(request):
    return HttpResponse('test1')

# Create your views here.

def home(request):
    
    return render(request,'proj1/index.html')


def test(request):
    return redirect(reverse('home'))
