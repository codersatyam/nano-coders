from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "tutorials/index.html")
def moretutorials1(request):
    return render(request, 'tutorials/moretutorials1.html')
def moretutorials2(request):
    return render(request, 'tutorials/moretutorials2.html')
def moretutorials3(request):
    return render(request, 'tutorials/moretutorials3.html')
def moretutorials4(request):
    return render(request, 'tutorials/moretutorials4.html')    
def htmldoc(request):
    return render(request, 'tutorials/htmldoc.html')        