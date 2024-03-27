from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from fikr_blog.models import IdeaBlog
from post.models import Photos
from user.models import Room


def home(request):
    rooms = Room.objects.all()
    ideas = IdeaBlog.objects.all().order_by('-created_time')
    photos = Photos.objects.all()
    return render(request, 'index.html', {'ideas': ideas, 'photos': photos, 'rooms': rooms})


def idea_blog(request):
    if request.user.is_authenticated:
        ideas = IdeaBlog.objects.all().order_by('-created_time')
        return render(request, 'idea.html', {'ideas': ideas})
    else:
        return HttpResponseRedirect(reverse('registration'))
