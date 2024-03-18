from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)


class IdeaBlog(BaseModel):
    title = models.CharField(max_length=250)
    body = models.TextField()

    class Meta:
        verbose_name = 'Idea Blog'
        verbose_name_plural = 'Idea Blogs'

    def __str__(self):
        return self.title
