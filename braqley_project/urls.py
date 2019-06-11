from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from django.conf.urls import url, include
from markdownx import urls as markdownx

urlpatterns = [
    path('', include('pages.urls')),
    url(r'^markdownx/', include('markdownx.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('posts/', include('posts.urls')),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]

