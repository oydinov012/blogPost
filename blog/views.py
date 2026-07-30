

from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.views import View
from blog.forms import PostForm, PostdeleteForm
from blog.models import Post, PostMedia
from comment.forms import CommentForm
from comment.models import Comment
from users.models import CustomUser

class PostListView(View):
    def get(self, req):
        post = Post.objects.filter(is_approved=True).order_by('-created_at')

        search_query = req.GET.get('q','')

        if search_query:
            post = post.filter(title__icontains=search_query)

        page_size = req.GET.get('page_size', 4)
        paginator = Paginator(post, page_size)

        page_num = req.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        return render(
            req,
            'post.html',
            {
                "post":post,
                "page_obj":page_obj
            }
        )


class PostDetailView(View):
    def get(self,req,id):
        post  = Post.objects.get(id=id)
        comment = Comment.objects.filter(blog=post).order_by('-created_at')
        form = CommentForm()
        return render(req,'post_detail.html',{"post":post,'form':form,'comments':comment})

    
class PostCreateView(LoginRequiredMixin,View):
    def get(self,req):
        form = PostForm() 
        return render(req,'post_create.html',{'form':form,})

    def post(self,req):
        form = PostForm(data=req.POST ,)
        if form.is_valid():
            post = form.save(commit=False) # type: ignore
            post.user = req.user
            post.save()
            files = req.FILES.getlist('media_files')
            
            for index, f in enumerate(files):
                if f.name.endswith(('.mp4', '.mkv', '.avi', '.mov')):
                    m_type = 'video'
                else:
                    m_type = 'image'
                
                PostMedia.objects.create(
                    blog=post,
                    file=f,
                    media_type=m_type,
                    is_cover=(index == 0) 
                )
            return redirect('post-list')
        return render(req,'post_create.html',{'form':form})


class PostUpdateview(LoginRequiredMixin,View):


    def get(self,req,id):
            user = req.user
            post = Post.objects.get(id=id)
            if post.user == user:
                postform = PostForm(instance=post)
                return render(req,'post_update.html',{"post":postform})
            return redirect('post-list')


    def post(self, req, id):
        post = Post.objects.get(id=id)
        if post.user == req.user:
            postform = PostForm(
                instance=post,
                data = req.POST,
                files=req.FILES
            )
            if postform.is_valid():
                postform.save() # type: ignore
                messages.success(req,'post malumotlari yangilandi')
                return redirect('post-detail',id=id)
            return render(req,'post_update.html',{"post":postform})
        
        return redirect('post-list')


class PostDeleteView(View):

            
            
    



    def get(self,req,id):
        post = Post.objects.get(id=id)
        if post.user == req.user:
            form = PostdeleteForm()
            return render(req,'post_delete.html',{"post":form})
        return redirect('post-detail')

    def post(self,req,id):
        post = Post.objects.get(id=id)
        if post.user == req.user:
            postdeleteform = PostdeleteForm(data=req.POST)
            if postdeleteform.is_valid():
                post.delete()
                messages.info(req,'post ochirildi')
                return redirect('post-list')
            return render(req,'post_delete.html',{"post":postdeleteform})


class PostAuthorListView(View):
    def get(self,req,id):
        user = CustomUser.objects.get(id=id)
        posts = Post.objects.filter(user=user)
        return render(req,'post_author_list.html',{"post":posts,"user":user})
