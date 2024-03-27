from django.contrib import admin
from .models import Contact, CustomUser, Profile, Signal, Room, Message

admin.site.register(Contact)
admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Room)
admin.site.register(Message)


@admin.register(Signal)
class SignalAdmin(admin.ModelAdmin):
    list_display = ('view_photo', 'created_time', 'updated_time')
    fields = ('view_photo',)

