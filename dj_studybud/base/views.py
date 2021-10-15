from django.shortcuts import render

# Create your views here.

rooms = [
    {'id':1, 'name': 'Lets learn python'},
    {'id':2, 'name': 'Design with me'}, 
    {'id':3, 'name': 'Frontend developers'},
]


#tworzenie nowej podstrony (widoku) podajemy jako argument HTTP request
#wersja właściwa: render - renderujemy coś zapisanego w pliku html
def home(request):
    context =  {'rooms': rooms}
    return render(request, 'base/home.html', context)  #podajemy rooms do template


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)
