from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    # adding the new field
    email = forms.EmailField(required=True)

    # configuration.. the model is the model that will be affected. fields are the fields you want to see and in which order
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']