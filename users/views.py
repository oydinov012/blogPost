from django.shortcuts import render ,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

from django.views import View
from .models import CustomUser
from .forms import UserCreateForm



class RegisterView(View):
    def get(self,req):
        register_form = UserCreateForm()
        return render(req, 'users/register.html',{"register_form":register_form})

    def post(self,req):
        register_form = UserCreateForm(data=req.POST)
        if register_form.is_valid():
            register_form.save()
            return render (req, 'home.html')
        return render(req, 'users/register.html',{"register_form":register_form})




class LoginView(View):
    def get(self,request):
        user_formq = AuthenticationForm()
        
        return render(request, 'users/login.html', {"aform": user_formq})

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
         
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)

        else:
            return render(request, 'users/login.html', {"aform": login_form})

        return render (request, 'home.html')