from django.contrib import messages

from django.db import IntegrityError
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

User = get_user_model()


def registration(request):
    if request.method == 'POST':
        # Formdan ma'lumotlarni olish
        username = request.POST.get('username').lower()
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        try:
            if len(password) < 4:
                raise ValueError("Parol 4 belgidan ko'p bolishi kerak.")
            if not phone.startswith('+') or not phone[1:].isdigit() or not (len(phone[1:]) == 12):
                raise ValueError("Telefon raqami xato.")
            if User.objects.filter(username=username).exists():
                raise ValueError("Bunday foydalanuvchi ro'yxatdan o'tgan.")
            if User.objects.filter(phone_number=phone).exists():
                raise ValueError("Bunday tel: raqami ro'yxatdan o'tgan.")
            # Foydalanuvchi obyekti yaratish
            user = User.objects.create_user(username=username, password=password, phone_number=phone)

            # Qo'shimcha ma'lumotlarni qo'shish
            user.profile.phone = phone  # Ehtimol, foydalanuvchi modelingizda phone maydoni mavjud bo'lishi kerak
            user.save()
            messages.success(request, "ro'xatdan o'tdingiz")

        except ValueError as ve:
            messages.error(request, str(ve))
        return redirect('registration')
    else:
        # GET so'rovi bo'lsa, shablonni ko'rsatish
        return render(request, 'registrations/login.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('usernamelogin').lower()
        password = request.POST.get('passwordlogin')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Muvoffaqiyatli kirish!')
            return redirect('home')  # O'zgartiring kerak bo'lsa
        else:
            messages.error(request, 'Noto‘g‘ri foydalanuvchi nomi yoki parol.')
    return render(request, 'registrations/login.html')


def login_photo(request):
    if request.method == 'POST':
        year = request.POST.get('year')
        month = request.POST.get('month')
        day = request.POST.get('day')
        password = year + month + day
        user = authenticate(request, username='asadbek', password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Muvoffaqiyatli kirish!')
            return redirect('photo')  # O'zgartiring kerak bo'lsa
        else:
            messages.error(request, "Afsuski bu tug'ilgan yil bilan kira olmaysiz")
    return render(request, 'registrations/registration.html')


def logout_user(request):
    logout(request)
    return redirect('home')
