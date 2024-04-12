from django.shortcuts import render

rooms=[
    {  'id':1,'name':'lets learn python'},
    {  'id':2,'name':'Design with me'},
    {  'id':3,'name':'Frontend developers'},

]

# Create your views here.
def home(request):
    contexts={'rooms':rooms}
    return render(request,'base/home.html',contexts)
def room(request,pk):
    return render(request,'base/room.html')

