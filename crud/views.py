from django.shortcuts import render
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

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

def insert(request):
    data_title= request.POST["title"]
    data_body= request.POST["body"]
    db_post=Post(title=data_title, content=data_body, pub_date=timezone.now())
    db_post.save()
    return HttpResponseRedirect(reverse("home"))

def post(request, id):
    db_post=Post.objects.get(pk=id)
    context={"post":db_post[::-1]}
    return render(request, "blog/post.html", context)