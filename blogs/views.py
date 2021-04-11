from django.shortcuts import render, HttpResponse, redirect
from .models import posts, blogcomments , create
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from django.core.mail import  EmailMessage
import threading

class emailthread(threading.Thread):
    def __init__(self,email_message):
        self.email_message=email_message
        threading.Thread.__init__(self)
    def run(self):
        self.email_message.send()

# Create your views here.
def home(request):
    allposts = posts.objects.all().order_by('sno')[::-1]
    
    context = {"allposts": allposts }
    return render(request, "blogs/home.html", context)
def content(request ,slug):
    post = posts.objects.filter(slug=slug).first()
    comments=blogcomments.objects.filter(post=post)
    length=comments.count()
    
    context = {"post": post , 'comments':comments, 'length':length, 'user':request.user }
    return render(request, "blogs/content.html", context)

def postcomments(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postsno = request.POST.get('postsno')
        post = posts.objects.get(sno=postsno)
         
        comment = blogcomments(comment=comment, user=user, post=post)
        comment.save()
        
        return redirect(f'/blogs/{post.slug}')
def own_blogs(request):
   return render(request,"blogs/own_blogs.html")
    
def make(request):
    if request.method == "POST":

        title=request.POST.get("title")
        username=request.user
       
        content=request.POST.get("content")
        email=request.user.email
        slug=request.POST.get("slug")
        submit= create(title=title,  content=content, email=email, slug=slug, username=username)
        
        email_message=EmailMessage(
            'thanks for create blog',
            'Your blog content will receive to the admin pannel',
            'codersnano@gmail.com',
            [email],
        )
        emailthread(email_message).start()
        submit.save()
        messages.success(request,"Your blog request will send to the admin successfully now wait for response")
        return redirect("/blogs")