from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout,authenticate, login
from .form import *
from .models import BlogModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

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
               messages.info(request,'Username or Password is incorrect ')

               return render(request,'login.html')
        
    return render(request,'login.html')


def logoutUser(request):
    logout(request)
    return redirect('index')

@login_required(login_url='login')
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

@login_required(login_url='login/')
def blog_detail(request,m_id):
   post=BlogModel.objects.get(pk=m_id)
   return render(request,'blog_detail.html',{'post':post})



def register_page(request):
    if request.method=='POST':
         username = request.POST['username']
         password1 = request.POST['password1']
         password2 = request.POST['password2']
         email=request.POST['email']
        
         if password1==password2:
             if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')
             elif User.objects.filter(email=email).exists():
                 messages.info(request,'Email already taken')
             else:    

                 user=User.objects.create_user(username=username,password=password1,email=email)
                 user.save()
                 print('user created')
                 return redirect('login')
         else:
             messages.info(request,'Password not matching ')

    return render(request, 'register_page.html')