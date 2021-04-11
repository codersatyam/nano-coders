from django.shortcuts import render 

# Create your views here.
def tools(request):
    return render(request, "tools/home.html")