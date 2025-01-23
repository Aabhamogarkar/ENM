from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate,login

# Create your views here.
def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    print('before if')
    if request.method == 'POST':   # Signup button pressed
        uname = request.POST.get('username')
        email=request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Passwords do not match")
        else:
            user = User.objects.create_user(username=uname,email=email,password=pass1)
        print('after if')
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')
        # return HttpResponse('User created successfully')
                

        # print(uname,email,pass1,pass2)
       
   
    return render(request,'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Invalid Credentials")
        # print(username,pass1)

    return render(request,'login.html')

# def logoutUser(request):
#     logout(request)
#     return redirect('login')
    