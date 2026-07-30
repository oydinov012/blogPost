from django.views import View
from comment.forms import CommentDeleteForm, CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post
from comment.models import Comment

class CommentList(View):
    def get(self, req, post_id):
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.filter(blog=post)
        return render(
            req,
            'post_detail.html',
            {
                "comments":comments,
                # "post":post
            }
        )
    
class CommetCreateView(LoginRequiredMixin, View):
    def get(self, req, post_id):
        return redirect('post-detail', id=post_id)

    def post(self, req, post_id):
        blog = get_object_or_404(Post, id=post_id)
        form = CommentForm(req.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = req.user
            comment.blog = blog
            comment.save()
            messages.success(req, "Kommentariya muvaffaqiyatli qo'shildi!")
        else:
            messages.error(req, "Xatolik yuz berdi, qaytadan urinib ko'ring.")
            
        return redirect('post-detail', id=post_id)


class CommentUpdateView(LoginRequiredMixin, View):
    def get(self, req, post_id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        post = get_object_or_404(Post, id=post_id)
        
        if req.user != comment.user:
            return redirect('post-detail', id=post_id)
            
        form = CommentForm(instance=comment)
        return render(req, 'post_detail.html', {"form": form, "post": post})

    def post(self, req, post_id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        post = get_object_or_404(Post, id=post_id)
        
        if req.user != comment.user:
            return redirect('post-detail', id=post_id)
            
        form = CommentForm(data=req.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(req, "Ma'lumotlar o'zgartirildi!")
            return redirect('post-detail', id=post_id)
            
        messages.info(req, "Ma'lumotlar mos kelmadi.")
        return render(req, 'post_detail.html', {"form": form, "post": post})


class CommetDeleteView(LoginRequiredMixin, View):
    def get(self,req,post_id,comment_id):
        if req.user==Comment.objects.get(id=comment_id).user:
            form = CommentDeleteForm()
            comment=Comment.objects.get(id=comment_id)
            return render(req,'comment_delete.html',{'form':form,'comment':comment})

        return redirect('post-detail',id=post_id)

    def post(self, req, post_id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if req.user == comment.user:
            comment.delete()
            messages.success(req, "Kommentariya o'chirildi!")
        return redirect('post-detail', id=post_id)