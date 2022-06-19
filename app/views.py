from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm

""" 
Authentication
"""

# --- Login --- #


def login_index(request):
    # Login
    if request.method == 'POST':
        # Get form values
        username = request.POST.get('username')
        password = request.POST.get('password')
        # User Existance
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        # Case user exist
        user = authenticate(request, username=username, password=password)
        # Credentials Testing
        if user is not None:
            login(request, user)
            return redirect('home_index')
        else:
            messages.error(request, 'User does not meet credentials')
    # Response
    response = {}
    return render(request, "app/Authentication/auth.html", response)


# --- Logout --- #
def logout_index(request):
    logout(request)
    return redirect('home_index')


""" 
Home Model
"""

# --- Index --- #


def home_index(request):
    # Get Rooms by Filter
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    # Get Topics
    topics = Topic.objects.all()
    # Response
    response = {"rooms": rooms, "topics": topics, "total_rooms": rooms.count()}
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
