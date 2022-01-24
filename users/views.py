from django.shortcuts import render,redirect
from django.views import View
from .forms import SignInForm , SignUpForm
from verify_email.email_handler import send_verification_email
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate


class Home(View):
    def get(self,request):
        return render(request,'home.html',status=200)

class SignIn(View):
    def get(self,request):
        form = SignInForm()
        return render(request,'users/sign_in.html',{'form':form},status=200)
    
    def post(self,request):    
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("user:home")
            else:
                messages.error(request,"Invalid username or password.")
                return render(request,'users/sign_in.html',{'form':form},status=200)
        else:
            messages.error(request,"Invalid username or password.")
            return render(request,'users/sign_in.html',{'form':form},status=200)

class SignUp(View):
    def get(self,request):
        form = SignUpForm()
        return render(request,'users/sign_up.html',context={'form':form},status=200)
    
    def post(self,request):
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            send_verification_email(request, form)
            messages.success(request, f"sending verify email to {form.cleaned_data['email']} email" )
            return render(request,template_name='home.html')
        else:
            return render(request,template_name='users/sign_up.html')
        