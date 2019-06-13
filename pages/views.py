from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from posts.models import Post


class HomePageView(TemplateView):
    template_name = 'home.html'

class Aj101Fall2019(TemplateView):
    template_name = 'aj101_fall2019.html'

class Ps324Fall2019(TemplateView):
    template_name = 'ps324_fall2019.html'

class CoursesPageView(TemplateView):
    template_name = 'courses.html'

# class MiscPageView(LoginRequiredMixin, ListView):
#     # model = Post
#     queryset = Post.objects.filter(topic="Research")
#     template_name = 'home2.html'
#     # login_url = 'login'

class MiscPageView(LoginRequiredMixin, TemplateView):
    template_name = 'home2.html'
    title = "My beautiful list of posts"

    def research_posts(self):
        return Post.objects.filter(topic="Research")

    def courses_posts(self):
        return Post.objects.filter(topic="Courses")

    def about_posts(self):
        return Post.objects.filter(topic="About")

