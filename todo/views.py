from django.shortcuts import render, redirect
from .models import Todo
from .forms import AddForm
from django.utils import timezone
import datetime

# Create your views here.
def delete_todo(request, pk):
    target = Todo.objects.get(pk=pk)
    target.delete()
    return redirect("todos")

def todo_view(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
    now = datetime.datetime.now()
    print(now)

    todos = Todo.objects.all()
    form = AddForm()
    data = {
        "todos":todos,
        "form":form,
        "now":now,
    }
    return render(request, "todo_list.html", data)

def nottodo_view(request):
    todos = Todo.objects.all()
    data = {
        "todos":todos,
    }
    return render(request, "nottodo_list.html", data)

def todo_done(request, pk):
    target = Todo.objects.get(pk=pk)
    target.is_done = True
    target.save()
    return redirect("todos")