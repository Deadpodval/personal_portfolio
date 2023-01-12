from django.shortcuts import render, get_object_or_404
from .models import User, Post


def all_blogs(request):
    users = User.objects.all()
    return render(request, 'blog/all_blogs.html', {'users': users})


def blog(request, blog_id: int):
    post = get_object_or_404(Post, pk=blog_id)
    return render(request, 'blog/detail.html', {'post': post})


def user_posts(request, user):
    user = User.objects.get(name=user)
    posts = Post.objects.order_by('-date')
    return render(request, 'blog/user_posts.html', {'user': user, 'posts': posts})


