from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    skills = ["Python", "Django", "HTML", "CSS", "JavaScript", "Bootstrap"]
    return render(request, "main/home.html", {"skills": skills})

def about(request):
    bio = "I am a passionate developer learning Django to build modern web apps."
    return render(request, "main/about.html", {"bio": bio})

def projects(request):
    project_list = [
        {"title": "Portfolio Website", "desc": "Personal website built in Django"},
        {"title": "Blog App", "desc": "Simple blog with CRUD features"},
        {"title": "E-commerce", "desc": "Shopping cart and payment integration"},
    ]
    return render(request, "main/projects.html", {"projects": project_list})

def contact(request):
    return render(request, "main/contact.html")
