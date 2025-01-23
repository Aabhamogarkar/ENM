from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate,login

# Create your views here.
def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    print('before if')
    if request.method == 'POST':
        uname = request.POST.get('username')
        email=request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        print('after if')

        print(uname,email,pass1,pass2)
       
   
    return render(request,'signup.html')

def LoginPage(request):
    return render(request,'login.html')

# def logoutUser(request):
#     logout(request)
#     return redirect('login')
    