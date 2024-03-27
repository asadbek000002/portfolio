from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import is_password_usable
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=13, unique=True, blank=True, null=True)

    def clean(self):
        super().clean()

        if self.phone_number and len(self.phone_number) < 10:
            raise ValidationError("Telefon raqami kamida 10 simvoldan iborat bo'lishi kerak.")

        if not is_password_usable(self.password):
            if not self.password.isdigit():
                raise ValidationError("Parol faqat sonlardan iborat bo'lishi kerak.")
            if len(self.password) != 4:
                raise ValidationError("Parol 4 ta sonlardan iborat bo'lishi kerak.")

        # Foydalanuvchi nomining unikaligini tekshirish
        if CustomUser.objects.filter(username=self.username).exists():
            raise ValidationError("Bu foydalanuvchi nomi mavjud. Boshqa nom kiriting.")


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)


# Post save signal
@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)


class Contact(BaseModel):
    chat = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.chat


class Signal(BaseModel):
    view_photo = models.IntegerField(default=0)


class Room(BaseModel):
    name = models.CharField(max_length=1000)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    user1 = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

    def __str__(self):
        return str(self.user)
