from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm


def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog})


def new(request):
    return render(request, 'new.html')


# def create(request):
#     new_blog = Blog()
#     new_blog.title = request.POST['title']
#     new_blog.content = request.POST['content']
#     new_blog.save()
#     return redirect('detail', new_blog.id)

def create(request):
    form = BlogForm(request.POST)
    # good case
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.save()
        return redirect('detail', new_blog.id)
    return render(request, 'new.html')


def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'edit_blog': edit_blog})


# def update(request, blog_id):
#     old_blog = get_object_or_404(Blog, pk=blog_id)
#     old_blog.title = request.POST['title']
#     old_blog.content = request.POST['content']
#     old_blog.save()
#     return redirect('detail', old_blog.id)

def update(request, blog_id):
    old_blog = get_object_or_404(Blog, pk=blog_id)
    form = BlogForm(request.POST, instance=old_blog)
    # good case
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.save()
        return redirect('detail', old_blog.id)
    # bad case
    return render(request, "new.html")


def delete(request, blog_id):
    delete_blog = get_object_or_404(Blog, pk=blog_id)
    delete_blog.delete()
    return redirect('home')
