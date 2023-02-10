from django.shortcuts import render

def home(request):

    context={

    }

    return render(request, "blog/index.html", context)