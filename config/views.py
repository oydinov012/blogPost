from django.views import View
from django.shortcuts import render , redirect


def home_page(request):

    return render(request,'home.html')