from django.contrib import admin
from .models import IdeaBlog, LikeIdea, Document

admin.site.register(IdeaBlog)
admin.site.register(Document)

@admin.register(LikeIdea)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'idea', 'cookie_id')
    fields = ['user', 'idea', 'cookie_id',]


