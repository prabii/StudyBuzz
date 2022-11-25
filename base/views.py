from multiprocessing import context
from django.shortcuts import render
from . models import Room



# rooms=[
#      {'id':1,'name':'Lets bang python'},    
#      {'id':2,'name':'Lets swipe devops'},     
#      {'id':3,'name':'Lets trigger study bot'},     


# ]
# Create your views here.

def home(request):
    rooms=Room.objects.all()
    context={'rooms':rooms}
    return render(request,'base/home.html',context)

def room(request ,pk):
    room = Room.objects.get(id=pk)

    context= {'room':room}
    return render(request,'base/room.html',context)