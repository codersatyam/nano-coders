from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,"ml/home.html")
def p1(request)    :
    return render(request,"ml/p1.html")
