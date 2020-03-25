from django.shortcuts import render
from .models import BlogArticle

def all_blogs(request):
    articles=BlogArticle.objects.all()
    return render(request, 'blog/blogs.html', {'articles' : articles})

# Create your views here.
