from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    return render(request,'index.html')

# process of creating an account
def signUp(request):
    if request.method == "POST":
        username= request.POST['username']
        Fname= request.POST['Fname']
        Lname= request.POST['Lname']
        email= request.POST['email']
        pw1= request.POST['pw1']
        pw2= request.POST['pw2']

        if User.objects.filter(username=username):
            messages.error(request, "username already exist.")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "Email already exsist.")

        if len(username)>12:
            messages.error(request, "username much be below 10 words")
        if pw1 != pw2:
            messages.error(request, "Password didn't match!")

        if not username.isa1num():
            messages.error(request, "Username must be Alpha-Numeric!")  
            return redirect('home')            

        myuser= User.objects.filter(username=username).first()
        myuser.save()
        messages.success(request,"your account is created successfully")
        return redirect('signIn')

# shows account is successfully create
    return render(request,"signUp.html")    

def signIn(request):
    if request.method == "POST":
        username=request.POST['username']
        pw1= request.POST['password']

        user=authenticate(username=username,password=pw1)

# if the user has an account
        if user is not None:
            login(request, user)
            fname= user.first_name
            return render(request, "index.html", {'fname':fname})
# if the password is not right thn error pops            
        else:
             messages.error(request, "Bad Credentials!")
            #  request redirect('home')

    return render(request,"signIn.html")    

def signOut(request):
   logout(request)
   messages.success(request, "Logged out successfully")
   return redirect('home')