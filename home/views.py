from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate, login
from .form import *
from .models import BlogModel
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login/')
def index(request):
    context= {'blogs':BlogModel.objects.all()}
    return render(request, 'index.html',context)




def loginUser(request):
    if request.method == "POST":
       username = request.POST['username']
       password = request.POST['password']
       if username and password:
          user = authenticate(username=username, password=password)
          print(username,password)
          if user:
             login(request, user)
             print (user)
             return redirect('index')
          else:
               return render(request,'login.html')
        
    return render(request,'login.html')


def logoutUser(request):
    logout(request)
    return redirect("login")

@login_required(login_url='login/')
def add_blog(request):
    if request.method=="POST":
       title=request.POST.get('title')
       content=request.POST.get('content')
       image= request.FILES['image']
       add_blog = BlogModel(title=title, content=content,image=image)
       User= request.user
       add_blog.save()
      
    return render(request,'add_blog.html')

@login_required(login_url='login/')
def blog_detail(request):
    context = {}
    try:
        blog_obj= BlogModel.objects.all()
        context['blog_obj']= blog_obj
    except Exception as e:
        print(e)

    return render(request,'blog_detail.html')


        


        
     
    
    

   
def logoutUser(request):
    logout(request)
    return redirect("login")

def add_blog(request):
    if request.method=="POST":
       title=request.POST.get('title')
       content=request.POST.get('content')
       image= request.FILES['image']
       add_blog = BlogModel(title=title, content=content,image=image)
       User= request.user
       add_blog.save()
       return redirect('index')
    

      
    return render(request,'add_blog.html')



def blog_detail(request):
    context = {}
    try:
        blog_obj= BlogModel.objects.all()
        context['blog_obj']= blog_obj
    except Exception as e:
        print(e)

    return render(request,'blog_detail.html')
