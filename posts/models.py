from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Post(models.Model):
    title = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class CoursePost(models.Model):
    title = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    body = MarkdownxField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    @property
    def formatted_markdown(self):
        return markdownify(self.text)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    
