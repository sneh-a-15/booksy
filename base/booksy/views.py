from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password != cpassword:
            return HttpResponse("Password and confirm password do no match!")
        else:
            my_user = User.objects.create_user(uname,email,password)
            my_user.save()
            return redirect('login')
    return render(request, 'signup.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=password1)
        if user is not None:
            print("a")
            login(request, user)
            print("b")
            return redirect('home')
        else:
            return HttpResponse("Username or Password Incorrect!")
    return render(request, 'login.html')

def Logout(request):
    logout(request)
    return redirect('login')