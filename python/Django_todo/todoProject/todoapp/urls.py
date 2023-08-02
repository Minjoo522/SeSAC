from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todo/", views.todo, name="todo"),
    path("create/", views.create_todo, name="create_todo"),
    # <int:pk>로 전달해도 됨
    path("todo/<int:todo_id>/", views.todo_description, name="todo_description"),
    path("update/<int:todo_id>/", views.update_todo, name="update_todo"),
    path("delete/", views.delete_todo, name="delete_todo"),
]
# HTML 메소드가 있어서 이런 url은 좋지 않음
# 💩 과도한 url이 만들어짐

# 🩷 RESTful하게 만들기(GET, POST, PUT, DELETE)
# 1. url을 각각 만들지 않고 detail에서 method == 'DELETE'로 delete를 구현하기!
# 2. 함수 이름도 generic하게 짓기!

# ✅ 리팩토링 과제 : 불필요한 CRUD 함수와 URL을 하나로 합치기!
# TOBE : todo/, todo/<tid>/만 남기기