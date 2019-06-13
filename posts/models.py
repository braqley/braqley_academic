from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from markdownx.admin import MarkdownxModelAdmin

from users.models import CustomUser


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
    module = models.CharField(max_length=255)
    body = MarkdownxField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    
    #Better option: just do separate model for each course-semester and limit module options in it
    #Then just need to have separate views (in pages and posts ) for each course that uses that model 
    # @property
    # def mod_choices(self):
    #     return self.author.available_mods

    @property
    def formatted_markdown(self):
        return markdownify(self.body)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Aj101Fall19Post(models.Model):
    MODULES = [("Intro", "Intro"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"), ("6", "6"), ("7", "7")]

    title = models.CharField(max_length=255)
    module = models.CharField(max_length=255, choices = MODULES)
    body = MarkdownxField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    @property
    def formatted_markdown(self):
        return markdownify(self.body)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('aj101_fall2019_post_detail', args=[str(self.id)])


