from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todo/", views.todo, name="todo"),
    path("create/", views.create_todo, name="create_todo"),
    path("todo/<int:todo_id>/", views.todo_description, name="todo_description"),
    path("update/<int:todo_id>/", views.update_todo, name="update_todo"),
    path("delete/", views.delete_todo, name="delete_todo"),
]