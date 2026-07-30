from django.urls import path, include
from comment.views import  CommentUpdateView, CommetDeleteView ,CommetCreateView, CommentList
urlpatterns = [
    path(
        '<int:post_id>/comment/create/',
        CommetCreateView.as_view(),
        name='comment-create',
    ),
    path(
        '<int:post_id>/comment/<int:comment_id>/update/',
        CommentUpdateView.as_view(),
        name='comment-update',
    ),
    path('post/<int:post_id>/comments/',CommentList.as_view(),name='comment-list'),
    path('post/<int:post_id>/delete/<int:comment_id>/',CommetDeleteView.as_view(),name='comment-delete')
    ]