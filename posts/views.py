from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Post, CoursePost



class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post_list.html'
    login_url = 'login'


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
    login_url = 'login'


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ('title', 'body',)
    template_name = 'post_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    # def dispatch(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     if obj.author != self.request.user:
    #         raise PermissionDenied
    #     return super().dispatch(request, *args, **kwargs)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    # def dispatch(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     if obj.author != self.request.user:
    #         raise PermissionDenied
    #     return super().dispatch(request, *args, **kwargs)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ('title', 'body')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


##################

class CoursePostListView(LoginRequiredMixin, ListView):
    model = CoursePost
    template_name = 'course_post_list.html'
    login_url = 'login'


class CoursePostDetailView(LoginRequiredMixin, DetailView):
    model = CoursePost
    template_name = 'course_post_detail.html'
    login_url = 'login'


class CoursePostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CoursePost
    fields = ('title', 'body',)
    template_name = 'course_post_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    # def dispatch(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     if obj.author != self.request.user:
    #         raise PermissionDenied
    #     return super().dispatch(request, *args, **kwargs)


class CoursePostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CoursePost
    template_name = 'course_post_delete.html'
    success_url = reverse_lazy('post_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    # def dispatch(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     if obj.author != self.request.user:
    #         raise PermissionDenied
    #     return super().dispatch(request, *args, **kwargs)


class CoursePostCreateView(LoginRequiredMixin, CreateView):
    model = CoursePost
    template_name = 'course_post_new.html'
    fields = ('title', 'body')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)