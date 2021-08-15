from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):  # передает цифровое значение
    blog = get_object_or_404(Blog, pk = blog_id) #pk первичный ключ (ищет обьект с даным id если его нет возращает ошибку)
    return render(request, 'blog/detail.html', {'blog': blog})  # передает в detail.html id ( blog_id)
