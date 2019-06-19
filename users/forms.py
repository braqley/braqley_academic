from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('name', 'email', 'course',)

    def signup(self, request, user):
        user.name = self.cleaned_data['name']
        user.email = self.cleaned_data['email']
        user.course = self.cleaned_data['course']
        user.save()

    


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'course',)