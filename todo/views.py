from django.shortcuts import render
from .models import Todo

# Create your views here.
def todo_view(request):
    todos = Todo.objects.all()
    data = {
        "todos":todos,
    }
    return render(request, "todo_list.html", data)

def nottodo_view(request):
    todos = Todo.objects.all()
    data = {
        "todos":todos,
    }
    return render(request, "nottodo_list.html", data)
