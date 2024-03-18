from django.shortcuts import render
from fikr_blog.models import IdeaBlog
from post.models import Photos


def home(request):
    ideas = IdeaBlog.objects.all().order_by('-created_time')
    photos = Photos.objects.all()
    return render(request, 'index.html', {'ideas': ideas, 'photos': photos})


def idea_blog(request):
    ideas = IdeaBlog.objects.all().order_by('-created_time')
    return render(request, 'idea.html', {'ideas': ideas})
