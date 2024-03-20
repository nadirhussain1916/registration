from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='home') 
def HomePage(request):
    return render(request, 'home.html')
    

def  SignupPage(request):
    # return render (request, 'signup.html')
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        my_user=User.objects.create_user(username, email, password1)
        my_user.save()
        return redirect('login')
        
        # if password1 != password2:
        #     print("Password is not same")
        # else:
            # my_user=User.objects.create_user(username, email, password1)
            # my_user.save()
            # return redirect('login')
    return render(request, 'signup.html')




def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("User name and password incorrect")
    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect ('login')
# Create your views here.
