# main/views.py

from django.shortcuts import render ,reverse
from .models import Resume

def home(request):
    return render(request, 'index.html')



def resume(request):
    resume = Resume.objects.first()
    return render(request, 'main/base.html', {'resume': resume})

