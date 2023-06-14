from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
# Create your views here.
def register(request):
    if request.method=='POST':
        un=request.POST['username']
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        em = request.POST['email']
        pwd=request.POST['password']
        pwd1 = request.POST['cpassword']
        if pwd==pwd1:
            if User.objects.filter(username=un).exists():
                messages.info(request,"username exists")
                return redirect('register')
            elif User.objects.filter(email=em).exists():
                messages.info(request,"mailid exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=un,first_name=fn,last_name=ln,email=em,password=pwd)
            user.save();
            return redirect('login')
            print("user created")
        else:
            messages.info(request,"password mismatch")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")