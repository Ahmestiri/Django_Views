from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

""" 
Home Model
"""

# Index
def home_index(request):
    rooms = Room.objects.all()
    response = {"rooms": rooms}
    return render(request, "app/index.html", response)


""" 
Room Model
"""

# Add
def room_add(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_index")
    response = {"form": form}
    return render(request, "app/Room/add.html", response)


# Edit
def room_edit(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home_index")
    response = {"form": form}
    return render(request, "app/Room/edit.html", response)


# View
def room_view(request, pk):
    room = Room.objects.get(id=pk)
    response = {"room": room}
    return render(request, "app/Room/view.html", response)


# Delete
def room_delete(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect("home_index")
    return render(request, "app/delete.html", {"object": room})
