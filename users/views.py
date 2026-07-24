import re

from django.shortcuts import render ,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages

from django.views import View

from .models import CustomUser
from .forms import UserCreateForm, UserUpdateForm



class RegisterView(View):
    def get(self,req):
        register_form = UserCreateForm()
        return render(req, 'users/register.html',{"register_form":register_form})

    def post(self,req):
        register_form = UserCreateForm(data=req.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('home-page')
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
            messages.success(request,'xush kelibsiz')
            return redirect('home-page')

        else:
            return render(request, 'users/login.html', {"aform": login_form})


class LogoutView(View):
    def get(self,req):
        logout(req)
        messages.info(req,"tizmdan chiqdingiz !!")
        return redirect('home-page')


class ProfilView(LoginRequiredMixin,View):
    def get(self, req):
        return render(req, 'user/profile.html', {'users':req.user})


class ProfilUpdateView(LoginRequiredMixin, View):
    def get(self,req):
        userupdateform = UserUpdateForm(instance=req.user)
        return render(req,'user/profilupdate.html', {"userform":userupdateform})


    def post(self,req):
        userupdateform = UserUpdateForm(
            instance=req.user,
            data=req.POST,
            files=req.FILES
        )
        if userupdateform.is_valid():
            user = userupdateform.save()
            update_session_auth_hash(req, user)
            messages.success(req,"profil malumotlari yangilandi")
            return redirect("profile-view")
        return render(req,'user/profilupdate.html', {"userform":userupdateform})


        