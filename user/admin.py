from django.contrib import admin
from .models import Contact, CustomUser, Profile

admin.site.register(Contact)
admin.site.register(CustomUser)
admin.site.register(Profile)
