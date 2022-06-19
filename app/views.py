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
# View
def room_view(request, pk):
    room = Room.objects.get(id=pk)
    response = {"room": room}
    return render(request, "app/Room/view.html", response)


# Delete
