from django.shortcuts import render
from projects.models import Project
from blog.models import BlogPost
from .models    import *


def home(request):

    posts = BlogPost.objects.filter(
        is_published=True
    ).order_by("-created_at")[:3]

    projects = Project.objects.all().order_by("-created_at")

    context = {
        "posts": posts,
        "projects": projects,
    }

    return render(
        request,
        "home.html",
        context
    )


def about(request):
    return render(request,"about.html")

def residential(request):
    return render(request, "services/residential.html")


def commercial(request):
    return render(request, "services/commercial.html")


def villa(request):
    return render(request, "services/villa.html")


def planning(request):
    return render(request, "services/planning.html")


def furniture(request):
    return render(request, "services/furniture.html")

def contact(request):
    return render(request,"contact.html")

from django.shortcuts import redirect
from .models import Consultation


def consultation(request):

    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Consultation.objects.create(
            name=name,
            phone=phone,
            email=email,
            message=message
        )

        return redirect("home")

    return redirect("home")


