from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from blog.models import Post

class PostListView(View):
    def get(self, req):
        post = Post.objects.filter(is_approved=True).order_by('id')

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
