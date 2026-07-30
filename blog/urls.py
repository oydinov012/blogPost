from django.urls import path , include
from blog.views import PostListView ,PostCreateView, PostUpdateview, PostDetailView, PostDeleteView, PostAuthorListView

urlpatterns = [
    path('',PostListView.as_view(),name='post-list'),
    path('<int:id>/',PostAuthorListView.as_view(),name='post-author-list'),
    path('<int:id>/detail/',PostDetailView.as_view(),name='post-detail'),
    path('create/',PostCreateView.as_view(),name='post-create'),
    path('<int:id>/update/',PostUpdateview.as_view(),name='post-update'),
    path('<int:id>/delete/',PostDeleteView.as_view(),name='post-delete'),
]