import uuid
from django.db import models
from user.models import CustomUser


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)


class ImportantEvents(BaseModel):
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='image/important_events')
    like = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        verbose_name = 'Important Event'
        verbose_name_plural = 'Important Events'

    def __str__(self):
        return self.title


class Photos(BaseModel):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/photos')

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    events = models.ForeignKey(ImportantEvents, on_delete=models.CASCADE, related_name='car_likes')
    cookie_id = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'events', 'cookie_id')
