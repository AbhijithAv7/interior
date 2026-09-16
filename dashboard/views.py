from django.shortcuts import render,redirect,get_object_or_404
from projects.models import Project
from .forms import ProjectForm
from projects.models import ProjectImage
from .forms import GalleryForm
from core.models import Consultation
from blog.models import BlogPost
from .forms import BlogPostForm
from core.models import Consultation




def dashboard(request):
    return render(request,"dashboard/dashboard.html")

def dashboard_projects(request):

    projects = Project.objects.all().order_by("-created_at")

    context = {

        "projects": projects

    }

    return render(
        request,
        "dashboard/dashboard_projects.html",
        context
    )


def add_project(request):

    if request.method=="POST":

        form=ProjectForm(request.POST,request.FILES)

        if form.is_valid():

            form.save()

            return redirect("dashboard_projects")

    else:

        form=ProjectForm()

    return render(

        request,

        "dashboard/add_project.html",

        {

            "form":form

        }

    )

def edit_project(request, id):

    project = get_object_or_404(Project, id=id)

    if request.method == "POST":

        form = ProjectForm(
            request.POST,
            request.FILES,
            instance=project
        )

        if form.is_valid():

            form.save()

            return redirect("dashboard_projects")

    else:

        form = ProjectForm(instance=project)

    return render(
        request,
        "dashboard/edit_project.html",
        {
            "form": form
        }
    )


def delete_project(request, id):

    project = get_object_or_404(Project, id=id)

    project.delete()

    return redirect("dashboard_projects")

def dashboard_gallery(request):

    images = ProjectImage.objects.select_related("project")

    return render(

        request,

        "dashboard/dashboard_gallery.html",

        {

            "images": images

        }
        
    )

def add_gallery(request):

    if request.method == "POST":

        form = GalleryForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            return redirect("dashboard_gallery")

    else:

        form = GalleryForm()

    return render(

        request,

        "dashboard/add_gallery.html",

        {

            "form": form

        }

    )

def delete_gallery(request,id):

    image = get_object_or_404(ProjectImage,id=id)

    image.delete()

    return redirect("dashboard_gallery")



def add_blog(request):

    if request.method == 'POST':

        form = BlogPostForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            from django.utils.text import slugify
            

            blog = form.save(commit=False)

            base_slug = slugify(blog.title)
            slug = base_slug
            counter = 1

            while BlogPost.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            blog.slug = slug

            blog.save()

            return redirect("blog_list")

    else:

        form = BlogPostForm()

    return render(
        request,
        'dashboard/add_blog.html',
        {
            'form': form
        }
    )

def edit_blog(request, id):

    blog = get_object_or_404(BlogPost, id=id)

    if request.method == "POST":

        form = BlogPostForm(
            request.POST,
            request.FILES,
            instance=blog
        )

        if form.is_valid():

            blog = form.save(commit=False)

            from django.utils.text import slugify

            base_slug = slugify(blog.title)
            slug = base_slug
            counter = 1

            while BlogPost.objects.filter(slug=slug).exclude(id=blog.id).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            blog.slug = slug
            blog.save()

            return redirect("dashboard_blog")

    else:

        form = BlogPostForm(instance=blog)

    return render(
        request,
        "dashboard/edit_blog.html",
        {
            "form": form,
            "blog": blog
        }
    )

def delete_blog(request, id):

    blog = get_object_or_404(BlogPost, id=id)

    if request.method == "POST":
        blog.delete()
        return redirect("dashboard_blog")

    return redirect("dashboard_blog")

def dashboard_blog(request):
    blogs = BlogPost.objects.all().order_by("-id")

    return render(
        request,
        "dashboard/dashboard_blog.html",
        {
            "blogs": blogs
        }
    )

def dashboard_messages(request):
    messages = Consultation.objects.all().order_by("-created_at")

    return render(
        request,
        "dashboard/dashboard_messages.html",
        {"messages": messages}
    )

