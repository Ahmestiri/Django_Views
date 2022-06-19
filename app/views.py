from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm

""" 
Home Model
"""

# --- Index --- #
def home_index(request):
    # Get Rooms by Filter
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    rooms = Room.objects.filter(topic__name__icontains=q)
    # Get Topics
    topics = Topic.objects.all()
    # Response
    response = {"rooms": rooms, "topics": topics}
    return render(request, "app/index.html", response)


""" 
Room Model
"""

# --- Add --- #
def room_add(request):
    # Create Room
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_index")
    # Reponse
    response = {"form": form}
    return render(request, "app/Room/add.html", response)


# --- View --- #
def room_view(request, pk):
    # Get Room by id
    room = Room.objects.get(id=pk)
    # Response
    response = {"room": room}
    return render(request, "app/Room/view.html", response)


# --- Edit --- #
def room_edit(request, pk):
    # Get Room by id
    room = Room.objects.get(id=pk)
    # Edit Room
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home_index")
    # Response
    response = {"form": form}
    return render(request, "app/Room/edit.html", response)


# --- Delete --- #
def room_delete(request, pk):
    # Get Room by id
    room = Room.objects.get(id=pk)
    # Delete Room
    if request.method == "POST":
        room.delete()
        return redirect("home_index")
    # Response
    response = {"object": room}
    return render(request, "app/delete.html", response)
