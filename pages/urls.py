from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about', views.AboutPageView.as_view(), name='about'),
    path('research', views.ResearchPageView.as_view(), name='research'),
    path('courses', views.CoursesPageView.as_view(), name='courses'),
    path('misc', views.MiscPageView.as_view(), name='misc'),
]