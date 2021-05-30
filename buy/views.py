from django.shortcuts import render, HttpResponse

# Create your views here.
def buyhome(request):
    return render(request, "buy/buyhome.html")
def sensor(request):
    return render(request,"buy/sensor.html")
