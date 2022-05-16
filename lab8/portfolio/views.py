#  hello/views.py
from django.http import HttpResponseRedirect
from django.shortcuts import render

#from .models import Tarefa
#from .forms import TarefaForm

from .models import Blog_Post
from .forms import BlogPostForm

from django.urls import reverse

# Create your views here.


def home_page_view(request):
    return render(request, 'portfolio/layout.html')

def about_me_page_view(request):
    return render(request, 'portfolio/about_me.html')

def blog_page_view(request):
    context = {'blog_posts': Blog_Post.objects.all()}
    return render(request, 'portfolio/blog.html', context)

def edita_blog_post_view(request, blog_post_id):
    blog_post = Blog_Post.objects.get(id=blog_post_id)
    form = BlogPostForm(request.POST or None, request.FILES, instance=blog_post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('blog'))

    context = {'form': form, 'blog_post_id': blog_post_id}
    return render(request, 'portfolio/edita.html', context)

def nova_blog_post_view(request):
    form = BlogPostForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('blog'))

    context = {'form': form}

    return render(request, 'portfolio/nova.html', context)