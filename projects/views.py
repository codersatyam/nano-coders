from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def python(request):
    return render(request, "projects/python.html")
def index(request):
    return render(request, "projects/index.html")
def cplus(request):
    return render(request, "projects/C++.html")
def java(request):
    return render(request, "projects/Java.html")
def p1(request):
    return render(request, 'projects/p1.html')
def p2(request):
    return render(request, 'projects/p2.html')
def p3(request):
    return render(request, 'projects/p3.html')
def p4(request):
    return render(request, 'projects/p4.html')
def p5(request):
    return render(request, 'projects/p5.html')
def p6(request):
    return render(request, 'projects/p6.html')
def p7(request):
    return render(request, 'projects/p7.html')
def p8(request):
    return render(request, 'projects/p8.html')
def p9(request):
    return render(request, 'projects/p9.html')
def p10(request):
    return render(request, 'projects/p10.html')                                
def p11(request):
    return render(request, 'projects/p11.html')
def p12(request):
    return render(request, 'projects/p12.html')        