from django.urls import path

from . import views

from posts import views as postviews

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('aj101_fall2019', views.Aj101Fall2019.as_view(), name='aj101_fall2019'),
    path('ps324_fall2019', views.Ps324Fall2019.as_view(), name='ps324_fall2019'),
    path('courses', views.CoursesPageView.as_view(), name='courses'),
    path('misc', views.MiscPageView.as_view(), name='misc'),
    path('aj101_fall2019/<int:pk>/', postviews.Aj101Fall19PostDetailView.as_view(), name='aj101_fall2019_post_detail'),
    path('aj101_fall2019/new_post/', postviews.Aj101Fall19PostCreateView.as_view(), name='aj101_fall2019_post_new'),
    path('aj101_fall2019/<int:pk>/edit_post/', postviews.Aj101Fall19PostUpdateView.as_view(), name='aj101_fall2019_post_edit'),
    path('aj101_fall2019/<int:pk>/delete_post/', postviews.Aj101Fall19PostDeleteView.as_view(), name='aj101_fall2019_post_delete'),
]