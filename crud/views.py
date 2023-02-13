from django.shortcuts import render
from .models import Post

def home(request):
    db_post=Post.objects.all()
    context={
        "posts":db_post
    }

    return render(request, "blog/index.html", context)

def write(request):
    context={
        
    }
    return render(request, "blog/write.html", context)