from django.shortcuts import render, get_object_or_404
from .models import Blogs
# Create your views here.

def allblogs(request):
    blogs=Blogs.objects
    return render(request,'blogs/allblogs.html',{'blogs':blogs})

def singlepost(request, blog_id):
    post = get_object_or_404(Blogs, pk=blog_id)
    return render(request,'blogs/singlepost.html',{'post':post})
