from django.forms import ModelForm
from .models import Room

"""
Room Form
"""


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"