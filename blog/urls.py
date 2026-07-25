from django.urls import path , include
from blog.views import PostListView

urlpatterns = [
    path('',PostListView.as_view(),name='post-list'),
]