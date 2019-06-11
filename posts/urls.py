from django.urls import path
from django.contrib import admin

from .views import (
#     PostListView,
#     PostUpdateView,
#     PostDetailView,
#     PostDeleteView,
#     PostCreateView,
#     CoursePostListView,
#     CoursePostUpdateView,
    CoursePostDetailView,
#     CoursePostDeleteView,
    CoursePostCreateView
        
)

urlpatterns = [
    path('<int:pk>/',
         CoursePostDetailView.as_view(), name='post_detail'),
#     path('<int:pk>/edit/',
#          CoursePostUpdateView.as_view(), name='post_edit'),
#     path('<int:pk>/delete/',
#          CoursePostDeleteView.as_view(), name='post_delete'),
    path('new/', CoursePostCreateView.as_view(), name='post_new'),
#     path('', CoursePostListView.as_view(), name='post_list'),
]

# from django.conf.urls import url

# urlpatterns = [
#     url(r'<int:pk>/$',
#          CoursePostDetailView.as_view(), name='post_detail'),
#     url(r'<int:pk>/edit/$',
#          CoursePostUpdateView.as_view(), name='post_edit'),
#     url(r'<int:pk>/delete/$',
#          CoursePostDeleteView.as_view(), name='post_delete'),
#     url(r'new/$', CoursePostCreateView.as_view(), name='post_new'),
#     url(r'', CoursePostListView.as_view(), name='post_list'),
# ]