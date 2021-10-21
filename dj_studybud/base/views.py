from django.shortcuts import render
from .models import Room
# Create your views here.

# rooms = [
#     {'id':1, 'name': 'Lets learn python'},
#     {'id':2, 'name': 'Design with me'}, 
#     {'id':3, 'name': 'Frontend developers'},
# ]




#tworzenie nowej podstrony (widoku) podajemy jako argument HTTP request
#wersja właściwa: render - renderujemy coś zapisanego w pliku html
def home(request):
    rooms = Room.objects.all()
    context =  {'rooms': rooms}
    return render(request, 'base/home.html', context)  #podajemy rooms do template


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


def createRoom(request):
    context = {}
    return render(request, 'base/room_form.html', context)