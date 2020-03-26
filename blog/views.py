from django.shortcuts import render, get_object_or_404
from .models import BlogArticle

def all_blogs(request):
    articles=BlogArticle.objects.all()
    return render(request, 'blog/blogs.html', {'articles' : articles})

def detail(request, article_id):
    article = get_object_or_404(BlogArticle, pk=article_id)
    return render(request, 'blog/detail.html',{'article': article})
# Create your views here.
