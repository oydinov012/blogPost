from blog.models import Post

from django.views import View
from django.shortcuts import render , redirect


class HomePageView(View):
    def get(self,req):
        post = Post.objects.order_by('-comment_count')[:3]
        return render(req,'home.html',{'posts':post})


class HelpView(View):
    def get(self,req):
        return render(req,'help.html')