from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import CoursePost, Aj101Fall19Post


admin.site.register(Aj101Fall19Post, MarkdownxModelAdmin)

admin.site.register(CoursePost)