import uuid

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from fikr_blog.models import IdeaBlog, LikeIdea
from post.models import Photos
from user.models import Room


def home(request):
    rooms = Room.objects.all()
    ideas = IdeaBlog.objects.all().order_by('-created_time')
    photos = Photos.objects.all()
    return render(request, 'index.html', {'ideas': ideas, 'photos': photos, 'rooms': rooms})


def idea_blog(request):
    ideas = IdeaBlog.objects.all().order_by('-created_time')
    cookie_id = request.COOKIES.get('cookie_id')
    liked_ideas = LikeIdea.objects.filter(cookie_id=cookie_id).values_list('idea_id', flat=True)

    for idea in ideas:
        idea.user_has_liked = idea.id in liked_ideas

    response = render(request, 'idea.html', {'ideas': ideas})

    if not cookie_id:
        cookie_id = str(uuid.uuid4())
        # Cookie ni 1 yilga saqlab qo'yish
        response.set_cookie('cookie_id', cookie_id, max_age=60 * 60 * 24 * 365)

    return response


def like_idea(request, id):
    idea = get_object_or_404(IdeaBlog, id=id)

    cookie_id = request.COOKIES.get('cookie_id')
    if not cookie_id:
        cookie_id = str(uuid.uuid4())

    user = request.user if request.user.is_authenticated else None
    liked = LikeIdea.objects.filter(idea=idea, cookie_id=cookie_id).exists()

    if liked:
        LikeIdea.objects.filter(idea=idea, cookie_id=cookie_id).delete()
        idea.like -= 1
        idea.save()
        response = JsonResponse({'status': 'unlike', 'like_count': idea.like})
    else:
        LikeIdea.objects.create(user=user, idea=idea, cookie_id=cookie_id)
        idea.like += 1
        idea.save()
        response = JsonResponse({'status': 'like', 'like_count': idea.like})

    if not request.COOKIES.get('cookie_id'):
        # Cookie ni 1 yilga saqlab qo'yish
        response.set_cookie('cookie_id', cookie_id, max_age=60 * 60 * 24 * 365)

    return response
