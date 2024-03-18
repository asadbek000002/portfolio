from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)


class ImportantEvents(BaseModel):
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='image/important_events')

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
