from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import choose, team


# Create your views here.
def demo(request):
    obj=choose.objects.all()
    obj1=team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})
def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user.auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
                return redirect('register')
            else:    
                user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
        
            user.save();
            print("user created")
            return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
    

# def calculator(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     res1=x-y
#     res2=x/y
#     res3=x*y
#     return render(request,"result.html",{'result':res,'result1':res1,'result2':res2,'result3':res3})

# def contact(request):
#     return render(request,"contact.html")
# def detail(request):
#     return render(request,"detail.html")
# def thanks(request):
#     return render(request,"thanks.html")
