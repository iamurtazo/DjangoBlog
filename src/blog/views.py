from django.shortcuts import render
from .models import Post
# from django.contrib.auth.models import User

def home(request):
    posts = Post.objects.all()
    # user = request.user
    context = {
        'title': 'Home Page',
        'posts': posts,
        # 'user': user,
    }

    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': 'About Page',
    }
    return render(request, 'blog/about.html', context)
