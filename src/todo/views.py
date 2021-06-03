from django.shortcuts import render, redirect, get_object_or_404

from .models import Todo
from .forms import TodoForm

# Create your views here.

#function based views FBV

def list_todo(request):
  #bringing all objects from todo
  todos = Todo.objects.all()
  return render(request, "list_todo.html", context={"todos": todos})


def new_todo(request):
  #if post request create form, else none
  form = TodoForm(request.POST or None)
  
  if form.is_valid():
      form.save()
      return redirect('todo:list-todo')

  return render(request, "new_todo.html", context={"form": form})


def update_todo(request, pk):
  #if no record found when searching for single object in db, not found error is given
  todo = get_object_or_404(Todo, pk=pk)
  form = TodoForm(request.POST or None, instance=todo)

  if form.is_valid():
      form.save()
      return redirect('todo:list-todo')

  return render(request, "update_todo.html", context={"form": form})


def delete_todo(request, pk):
  todo = get_object_or_404(Todo, pk=pk)

  if request.method == 'POST':
      todo.delete()
      return redirect('todo:list-todo')

  return render(request, "delete_todo.html", context={})
