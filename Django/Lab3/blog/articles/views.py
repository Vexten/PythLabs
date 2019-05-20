from django.shortcuts import render
from .models import Article

def arch(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

# Create your views here.
