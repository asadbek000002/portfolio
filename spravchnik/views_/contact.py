import random
from django.urls import reverse
from django.shortcuts import render, redirect
from user.models import Room, Message
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect


def contact_create(request):
    return render(request, 'contact.html')


def room_(request, room):
    room_details = Room.objects.get(name=room)
    username = room_details.user

    return render(request, 'contact.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })


def checkview(request):
    if request.user.is_authenticated:
        current_user = request.user
        username = current_user.username
        room = None  # room o'zgaruvchisini boshlang'ich qiymat bilan tanlang

        # Room obyektini yaratish yoki mavjud bo'lganini tekshirish
        room_if = Room.objects.filter(user=current_user).first()

        # Agar foydalanuvchiga allaqachon bir xona berilgan bo'lsa
        if room_if:
            room = room_if.name  # room o'zgaruvchisini aniqlash
        else:
            # Yangi xona yaratish
            room_name = ''.join(random.choices('0123456789', k=7))
            new_room = Room.objects.create(name=room_name, user=current_user)
            new_room.save()
            room = new_room.name  # room o'zgaruvchisini aniqlash

        return redirect('/' + room + '/?username=' + username)
    else:
        return HttpResponseRedirect(reverse('login'))


def send(request):
    message = request.POST['message']
    current_user = request.user
    user = current_user
    room_id = request.POST['room_id']
    print(room_id)

    new_message = Message.objects.create(value=message, user1=user, user=user, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def getMessages(request, room):
    if request.user.is_authenticated:
        room_details = Room.objects.get(name=room)
        messages = Message.objects.filter(room=room_details.id).values('value', 'date', 'user1')
        return JsonResponse({"messages": list(messages.values())})
    else:
        return HttpResponseRedirect(reverse('login'))


def get_room(request):
    rooms = Room.objects.all()
    print(rooms)
    return render(request, 'room.html', {'rooms': rooms})
