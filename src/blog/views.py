from django.shortcuts import render

posts = [
    {
        'author': 'John Smith',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2024'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2024'
    }
]

# Create your views here.
def home(request):
    context = {
        'title': 'Home Page',
        'posts': posts
    }

    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': 'About Page',
    }
    return render(request, 'blog/about.html', context)
