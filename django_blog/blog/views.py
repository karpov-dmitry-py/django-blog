from django.shortcuts import render
from .models import Post

# posts = [
#
#     {
#         'author': 'Dmitry Karpov',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'March 28, 2020'
#     },
#     {
#         'author': 'John Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'March 27, 2020',
#     }
#
# ]

def home(request):
    context = {'posts': Post.objects.all(), 'title': 'Home page' }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {'title': 'About page'}
    return render(request, 'blog/about.html', context)