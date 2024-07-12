import uuid
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse

from post.models import ImportantEvents, Photos, Like
from user.models import Signal


def important_events(request):
    events = ImportantEvents.objects.all()
    cookie_id = request.COOKIES.get('cookie_id')
    for event in events:
        event.user_has_liked = Like.objects.filter(events=event, cookie_id=cookie_id).exists()
    return render(request, 'post.html', {'events': events})


def events_detail(request, id):
    event = ImportantEvents.objects.get(id=id)
    return render(request, 'post_detail.html', {'event': event})


def photo(request):
    if request.user.is_authenticated:
        if request.user.username == "dilnora" or request.user.username == "asadbek":
            if request.user.username == "dilnora":
                signal_object = Signal.objects.order_by('-id').first()
                signal_object.view_photo += 1
                Signal.objects.create(view_photo=signal_object.view_photo)
            photos = Photos.objects.all()
            return render(request, 'photo.html', {'photos': photos})
        else:
            return HttpResponseRedirect(reverse('login_photo'))

    else:
        return HttpResponseRedirect(reverse('login'))


def like(request, id):
    events = get_object_or_404(ImportantEvents, id=id)

    # Foydalanuvchini aniqlash uchun cookie ni olish yoki yaratish
    cookie_id = request.COOKIES.get('cookie_id')
    if not cookie_id:
        cookie_id = str(uuid.uuid4())

    user = request.user if request.user.is_authenticated else None

    liked = Like.objects.filter(events=events, cookie_id=cookie_id).exists()

    if liked:
        # User already liked the event, so unlike it
        Like.objects.filter(events=events, cookie_id=cookie_id).delete()
        events.like -= 1
        events.save()
        response = JsonResponse({'status': 'unlike', 'like_count': events.like})
    else:
        # User has not liked the event yet, so like it
        Like.objects.create(user=user, events=events, cookie_id=cookie_id)
        events.like += 1
        events.save()
        response = JsonResponse({'status': 'like', 'like_count': events.like})

    # Foydalanuvchi cookie si mavjud bo'lmasa, yangi cookie yaratish
    if not request.COOKIES.get('cookie_id'):
        response.set_cookie('cookie_id', cookie_id)

    return response

