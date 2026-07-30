import re

from django.views import View
from django.shortcuts import render , redirect


def home_page(request):

    return render(request,'home.html')


class HelpView(View):
    def get(self,req):
        return render(req,'help.html')