from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from post.models import ImportantEvents, Photos
from user.models import Signal


def important_events(request):
    events = ImportantEvents.objects.all()
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
