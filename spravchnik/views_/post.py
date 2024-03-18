from django.shortcuts import render
from post.models import ImportantEvents, Photos


def important_events(request):
    events = ImportantEvents.objects.all()
    return render(request, 'post.html', {'events': events})


def events_detail(request, id):
    event = ImportantEvents.objects.get(id=id)
    return render(request, 'post_detail.html', {'event': event})


def photo(request):
    photos = Photos.objects.all()
    return render(request, 'photo.html', {'photos': photos})
