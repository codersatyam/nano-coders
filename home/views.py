from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from blogs.models import posts,blogcomments
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
import threading

class emailthread(threading.Thread):
    def __init__(self,email_message):
        self.email_message=email_message
        threading.Thread.__init__(self)
    def run(self):
        self.email_message.send()

# Create your views here.
def home(request):
    nano=authenticate( request, )
    if nano == 'coder123':
        check='nanocoder'
        param={'check':check}
        return render(request, "home/home.html", param)
    else:
         return render(request, "home/home.html")   
def about(request):
    return render(request, "home/about.html")
def contact(request):
     return render(request, "home/contact.html")
def search(request):
    query=request.GET['query']
    if len(query) >80:
        allpost=[]
    else:    
        allposttitle= posts.objects.filter(title__icontains = query)
        allpostcontent= posts.objects.filter(content__icontains = query)
        allpost=allposttitle.union(allpostcontent)
        global time
        time=allpost.count()
    params= {"allpost" : allpost, 'query':query , 'time':time}
    return render(request, "home/search.html", params)
def signup(request):
     if request.method == "POST":
# get all the post parameter
         username = request.POST['username']
         firstname = request.POST['firstname']
         lastname = request.POST['lastname']
         password = request.POST['password']
         email = request.POST['email']
         confirmpassword = request.POST['confirmpassword']
         confirmemail=User.objects.filter(email=email).first()
 # check some conditions
         if len(username) > 10:
             messages.error(request, "hy ")
             return redirect("home1")
         if password != confirmpassword:
             messages.error(request, "password not match")
             return  redirect("home1")
         if confirmemail is  not None:
             messages.error(request, ' This email is already use.Please choose another email to signup Nano Coders')
             return redirect('home1')
         if not username.isalnum():
             messages.error(request, "User name should contain number and characters")
             return redirect("home1")
  # create the user
         myuser = User.objects.create_user(username, email, password)
         myuser.first_name = firstname
         myuser.last_name = lastname
         # send email to the user
         email_message=EmailMessage(
             'Thanks for signup to NanoCoders',
             'message body',
             'codersnano@gmail.com',
             [email],
             
             )
         emailthread(email_message).start()
         myuser.save()
         messages.success(request, "successsfuly created")
         
         return redirect('home1')
   
         
     else :
         return HttpResponse("not found")
def handlelogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
          
            messages.success(request, "successful login")
            return redirect('home1')
        else:
            messages.error(request, "inavlid credations")
            return redirect('home1')
    else:
        return HttpResponse("404 error")

def handlelogout(request):
    logout(request)
    messages.success(request, 'Successfully logout')
    return redirect('home1')
def tools(request):
    return render(request, 'tools/thome.html')


