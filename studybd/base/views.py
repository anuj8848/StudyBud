from django.shortcuts import render,redirect
from django.db.models import Q

from django.contrib import messages

from django.contrib.auth.models import User

from .models import Room,Topic
from .forms import RoomForm

from django.contrib.auth import authenticate,login,logout

# rooms=[
#     {  'id':1,'name':'lets learn python'},
#     {  'id':2,'name':'Design with me'},
#     {  'id':3,'name':'Frontend developers'},

# ]

# Create your views here.

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
    
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,"user doesn't exist!!!")
            
        user=authenticate(request,username=username, password=password)
    
        if user is not None:
            login(request,user)
            return redirect('home')
        
        else:
            messages.error(request,'username or password does not exist!!!')
    contexts={}  
    return render(request,'base/login_register.html',contexts)
        

#logout
def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    
    q=request.GET.get('q') if request.GET.get('q')!=None else ""
    
    
    rooms=Room.objects.filter(
                              Q(topic__name__icontains=q) |
                              Q(name__icontains=q) |
                              Q(description__icontains=q))# case insensitive
    room_count=rooms.count()
    topics=Topic.objects.all()
    contexts={'rooms':rooms,'topics':topics,'room_count':room_count}
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

def updateRoom(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)
    contexts={'form':form}
    return render(request,'base/room_form.html',contexts)


def deleteRoom(request,pk):
    room=Room.objects.get(id=pk)
    if request.method=='POST':
        room.delete()
        return redirect('home')
    return render(request,'base/deletes.html',{'obj':room})