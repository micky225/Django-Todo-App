from django.shortcuts import render, redirect
from .models import TodoModel
from api.models import Todo
from django.http import HttpResponse
# Create your views here.
def home(request):
    todos = Todo.objects.all()

    context = {"todos":todos}
    return render(request, 'index.html', context)


def createTodo(request):
    if request.method == "POST":
        name = request.POST.get("name")  
        description = request.POST.get("description")  
        new_todo = Todo.objects.create(name=name, description=description)
        new_todo.save()
        return redirect("todo:home")



def updateTodo(request):
    if request.method == "POST":
        name = request.POST.get("todo_id")
        update_todo = Todo.objects.get(id=name)
        update_todo.done = True
        update_todo.save()
        return redirect("todo:home")


def deleteTodo(request):
    if request.method == "POST":
        name = request.POST.get("todo_id")
        delete_todo = Todo.objects.get(id=name)
        delete_todo.delete()
        return redirect ("todo:home")        

