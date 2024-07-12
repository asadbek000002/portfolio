import uuid

from django.db import models

from user.models import CustomUser


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)


class IdeaBlog(BaseModel):
    title = models.CharField(max_length=250)
    body = models.TextField()
    like = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        verbose_name = 'Idea Blog'
        verbose_name_plural = 'Idea Blogs'

    def __str__(self):
        return self.title


class LikeIdea(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    idea = models.ForeignKey(IdeaBlog, on_delete=models.CASCADE, related_name='idea_likes')
    cookie_id = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'idea', 'cookie_id')
