from django.contrib import admin
from .models import IdeaBlog, LikeIdea

admin.site.register(IdeaBlog)

@admin.register(LikeIdea)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'idea', 'cookie_id')
    fields = ['user', 'idea', 'cookie_id',]


