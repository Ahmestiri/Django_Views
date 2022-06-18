from django.db import models


class Room(models.Model):
    # Database Columns
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # Print Room
    def __str__(self):
        return str(self.name)


class Message(models.Model):
    # Database Columns
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # Print Room
    def __str__(self):
        return str(self.body[0:50])
