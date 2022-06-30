from django.forms import ModelForm
from .models import User, Room
from django.contrib.auth.forms import UserCreationForm


"""
Register Form
"""


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


"""
User Form
"""


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'image', 'bio']


"""
Room Form
"""


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        exclude = ['host', 'participants']
