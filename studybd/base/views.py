from django.shortcuts import render
from .models import Room
rooms=[
    {  'id':1,'name':'lets learn python'},
    {  'id':2,'name':'Design with me'},
    {  'id':3,'name':'Frontend developers'},

]

# Create your views here.
def home(request):
    rooms=Room.objects.all()
    contexts={'rooms':rooms}
    return render(request,'base/home.html',contexts)
def room(request,pk):
    room=None
    for i in rooms:
        if i['id']==int(pk):
            room=i
    contexts={'room':room}
    return render(request,'base/room.html',contexts)
