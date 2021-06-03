from django.urls import path

from .views import list_todo, update_todo, new_todo, delete_todo

app_name = "todo"

urlpatterns = [
    #when nothing is given, give us view of list_todos
    path("", list_todo, name="list-todo"),
    path("new-todo", new_todo, name="new-todo"),
    path("update-todo/<int:pk>", update_todo, name="update-todo"),
    path("delete-todo/<int:pk>", delete_todo, name="delete-todo"),

]