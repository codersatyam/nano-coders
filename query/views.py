from django.shortcuts import render, redirect
from query.models import query
# Create your views here.
def issue(request):
     if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        content=request.POST.get('content')
        submit=query(username=username, email=email, content=content)
        submit.save()
        return redirect('/blogs')


def solution(request):
     return render(request, 'query/solution.html')
def lr(request):
     return render(request,'courses/lr.html')
def ml(request):
     return render(request,'courses/ml.html')
def pr(request)     :
     return render(request,'courses/pr.html')          
def dt(request)     :
     return render(request,'courses/dt.html')
def r2(request)     :
     return render(request,'courses/r2.html')
def rf(request)     :
     return render(request,'courses/rf.html')
def bestr(request)     :
     return render(request,'courses/bestr.html')     
def preprocessing(request)     :
     return render(request,'courses/datapreprocessing/preprocessing.html')
def variables(request)     :
     return render(request,'courses/datapreprocessing/variables.html')
def usefulfunctions(request)     :
     return render(request,'courses/datapreprocessing/usefulfunctions.html')
def calldataset(request)     :
     return render(request,'courses/datapreprocessing/dataset.html')
def m(request)     :
     return render(request,'courses/datapreprocessing/m.html')
def ignoringrow(request)     :
     return render(request,'courses/datapreprocessing/ignoringrow.html')
def mm(request)     :
     return render(request,'courses/datapreprocessing/mm.html')
def mmc(request)     :
     return render(request,'courses/datapreprocessing/mmc.html')
def sklearn(request)     :
     return render(request,'courses/datapreprocessing/sklearn.html')
def sklearnd(request)     :
     return render(request,'courses/datapreprocessing/sklearnd.html')
def missingdata(request)     :
     return render(request,'courses/datapreprocessing/datacleaning.html')      
def steps(request)     :
     return render(request,'courses/datapreprocessing/steps.html')   
def dpa(request)     :
     return render(request,'courses/deeplearning/dpa.html') 
def introduction(request)     :
     return render(request,'courses/python/introduction.html')
def pvariables(request)     :
     return render(request,'courses/python/variables.html')                                                                                  
def ptype(request)     :
     return render(request,'courses/python/typeconversion.html')                                                                                  
def poperators(request)     :
     return render(request,'courses/python/operators.html')                                                                                  
def pconditional(request)     :
     return render(request,'courses/python/ifelse.html')                                                                                  
def ploop(request)     :
     return render(request,'courses/python/loops.html')                                                                                  
def pinput(request)     :
     return render(request,'courses/python/input.html')                                                                                  
def pstring(request)     :
     return render(request,'courses/python/string.html')                                                                                  
def plist(request)     :
     return render(request,'courses/python/list.html')                                                                                  
def pdictonary(request)     :
     return render(request,'courses/python/dictonary.html')                                                                                  
def ptuples(request)     :
     return render(request,'courses/python/tuple.html')                                                                                  
def pset(request)     :
     return render(request,'courses/python/set.html')                                                                                  
def pfunctions(request)     :
     return render(request,'courses/python/functions.html')                                                                                  

