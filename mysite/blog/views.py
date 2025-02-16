from django.shortcuts import render, get_object_or_404  # Fixed import statement
from .models import Post  # Fixed import path
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)  # 3 posts per page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})

def post_list(request):
    posts = Post.objects.filter(status='published')  # Fixed assignment operator and query
    return render(request, 'blog/post/list.html', {'posts': posts})  # Fixed dictionary syntax

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', 
                             publish__year=year, publish__month=month, publish__day=day)  # Fixed field lookups
    return render(request, 'blog/post/detail.html', {'post': post})  # Fixed string and dictionary syntax


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

