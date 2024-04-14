from django.shortcuts import render,redirect
from .models import Room
from .forms import RoomForm

# rooms=[
#     {  'id':1,'name':'lets learn python'},
#     {  'id':2,'name':'Design with me'},
#     {  'id':3,'name':'Frontend developers'},

# ]

# Create your views here.
def home(request):
    rooms=Room.objects.all()
    contexts={'rooms':rooms}
    return render(request,'base/home.html',contexts)
def room(request,pk):
    room=Room.objects.get(id=pk)
    contexts={'room':room}
    return render(request,'base/room.html',contexts)

def createRoom(request):
    form=RoomForm()
    if request.method=='POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    contexts={'form':form}
    return render(request,'base/room_form.html',contexts)

