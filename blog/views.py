from django.shortcuts import render, redirect
from blog.models import Category, Post
from blog.forms import AddBlogForm

def category(request):
    category = Category.objects.all()
    return category

def blog(request):
    blogs = Post.objects.all()
    context = {
        'blogs':blogs,
        'category':category(request)
    }
    return render(request, 'blog/blog.html', context)

def add_blog(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = AddBlogForm(request.POST,request.FILES)
            if fm.is_valid():
                form = fm.save(commit=False)
                form.author = request.user
                form.save()
                return redirect('d')
            return render(request, 'blog/uploadblogs.html', {'form':fm, 'category':category(request)})
        else:
            fm = AddBlogForm()
            return render(request, 'blog/uploadblogs.html', {'form':fm, 'category':category(request)})
    else:
        return redirect('l')

def blog(request):
    blogs = Post.objects.all()
    context = {
        'blogs':blogs,
        'category':category(request)
    }
    return render(request, 'blog/blog.html', context)

def read_post(request, slug):
    blog = Post.objects.get(slug=slug)
  
    context = {
        'blog':blog,
        'category':category(request),
        }
        
    return render(request, 'blog/readblog.html', context)

def my_blog_post(request):
    if request.user.is_authenticated:
        blogs = Post.objects.filter(author=request.user).order_by('-add_date')
        return render(request, 'blog/myblogs.html',  {'blogs':blogs, 'category':category(request)})
    else:
        return redirect('l')

def my_draft_blog_post(request):
    if request.user.is_authenticated:
        blogs = Post.objects.filter(author=request.user).order_by('-add_date')
        return render(request, 'blog/draftblogs.html',  {'blogs':blogs, 'category':category(request)})
    else:
        return redirect('l')

def blog_category(request, slug):
    blog_category = Category.objects.get(slug=slug)
    blogs = Post.objects.filter(category=blog_category)
    context = {
        'blog_category':blog_category,
        'blogs':blogs,
        'category':category(request)
    }
    return render(request, 'blog/category.html', context)
