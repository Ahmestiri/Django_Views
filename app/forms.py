from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User

"""
Room Form
"""


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        exclude = ['host', 'participants']


"""
User Form
"""


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
