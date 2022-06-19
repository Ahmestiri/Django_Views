from django.db import models
from django.contrib.auth.models import User

""" 
Topic Model
"""


class Topic(models.Model):
    # Database Columns
    name = models.CharField(max_length=200)
    # Print Topic
    def __str__(self):
        return str(self.name)


""" 
Room Model
HasOne Topic
HasOne User
"""


class Room(models.Model):
    # Database Columns
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # Order Rooms
    class Meta:
        ordering = ["-updated", "-created"]

    # Print Room
    def __str__(self):
        return str(self.name)


""" 
Message Model
HasOne User
HasOne Room
"""


class Message(models.Model):
    # Database Columns
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # Print Message
    def __str__(self):
        return str(self.body[0:50])
