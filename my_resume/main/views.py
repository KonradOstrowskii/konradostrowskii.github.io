# main/views.py

from django.shortcuts import render ,reverse
from .models import Resume


def index(request):
    experience = "Two years of experience in web development"
    projects = ["Project A", "Project B", "Project C"]
    context = {
        'experience': experience,
        'projects': projects
    }
    return render(request, 'base.html', context=context)


def resume(request):
    resume = Resume.objects.first()
    return render(request, 'main/base.html', {'resume': resume})

