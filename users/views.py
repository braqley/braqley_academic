from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.shortcuts import redirect
from .models import CustomUser
from django.http import HttpResponseRedirect, HttpRequest


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def login_success(request):
    if CustomUser.objects.get(id = request.user.id).course == "AJ101 Fall 2019":
        return redirect("aj101_fall2019")
    if CustomUser.objects.get(id = request.user.id).course == "PS324 Fall 2019":
        return redirect("ps324_fall2019")
    else:
        return redirect("home")


def logout_success(request):
    return redirect("login")
    #for remaining on page:
    # return redirect(request.META['HTTP_REFERER'])