from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from datetime import datetime

def home(request):
    return render (request, "index.html")

def todo(request):
    todos = Todo.objects.all()
    return render(request, "todo.html", {'todos': todos})

def create_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        create_date = datetime.now()
        Todo.objects.create(title=title, content=content, create_date=create_date, update_date=None)
        return redirect('todo')
    return render(request, "create_todo.html")

def todo_description(request, todo_id):
    # todo = Todo.objects.get(id=todo_id)
    # ✨ get_object_or_404 : 없는 페이지에 접근하는 경우 404 페이지를 띄워주기 위해서
    # RESTful 하게 처리하기
    # if request.method == 'DELETE':
    #     _task_delete(request, pk)
    # elif request.method == 'GET':
    #     _task_update(request, pk)
    todo = get_object_or_404(Todo, id=todo_id)
    return render(request, "todo_description.html", {'todo': todo})

def update_todo(request, todo_id):
    # todo = Todo.objects.get(id=todo_id)
    # ✨ get_object_or_404 : 없는 페이지에 접근하는 경우 404 페이지를 띄워주기 위해서
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        new_title = request.POST['new_title']
        new_content = request.POST['new_content']
        update_date = datetime.now()
        todo.title = new_title
        todo.content = new_content
        todo.update_date = update_date
        todo.save()
        return redirect('todo_description', todo_id=todo.pk)
    return render(request, "update_todo.html", {'todo': todo})

def delete_todo(request):
    todo_id = request.POST['todo_id']
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo')