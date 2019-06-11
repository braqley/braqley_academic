from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import CoursePost

admin.site.register(CoursePost, MarkdownxModelAdmin)
