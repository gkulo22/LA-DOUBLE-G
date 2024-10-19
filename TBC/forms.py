from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='ელ-ფოსტა')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'password1': 'პაროლი',
            'password2': 'გაიმეორე პაროლი',
            'username': 'მომხმარებლის სახელი',
        }