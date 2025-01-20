from django.shortcuts import render
from .models import Post, Category

def HomePage(request):
    return render(request, 'tech-index.html')

def Categorya1(request):
    return render(request, 'tech-category-01.html')

def Categorya2(request):
    return render(request, 'tech-category-02.html')

def Categorya3(request):
    return render(request, 'tech-category-03.html')

def Contact(request):
    return render(request, 'tech-contact.html')

def Single(request):
    return render(request, 'tech-single.html')

def Author(request):
    return render(request, 'tech-author.html')

def CategorysView(request, slug):
    cat = Category.objects.get(slug=slug)
    malumotlar = Post.published.filter(category=cat)
    return render(request, 'navbar.html', {'malumotlar': malumotlar, 'cat': cat})