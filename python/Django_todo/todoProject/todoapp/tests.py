from django.test import TestCase
from django.urls import reverse
from .models import Todo

# 클래스 이름 뒤에 Tests라고 하는 게 일반적
# 함수 이름 앞에 test라고 하는 게 일반적
class TodoModelTests(TestCase):
    def test_str_representation(self):
        todo = Todo.objects.create(title="Test Todo", content="테스트하기 위한 나의 Todo 항목")
        # 내가 원하는 테스트 케이스가 잘 작동하는지 확인하기 위한 구문
        self.assertEqual(str(todo), "Test Todo")

# 뷰 페이지 테스트
class TodoViewTests(TestCase):
    def test_todo_list_view(self):
        # ✨ 함수의 url을 거꾸로 가져와서 잘 실행 되는지 보고자 셋업
        response = self.client.get(reverse("todo"))
        self.assertEqual(response.status_code, 200)
        # ✨ html 파일을 잘 매칭해서 불러오고 있는지 확인
        self.assertTemplateUsed(response, "todo.html")
        # print(response)
        # .<HttpResponse status_code=200, "text/html; charset=utf-8">
        # print(response.status_code)
        # 200
        # print(response.content)
        # b'<!DOCTYPE html>\n<html lang="en">\n  <head>\n    <meta charset="UTF-8" />\n    <meta name="viewport" content="width=device-width, initial-scale=1.0" />\n    <link\n      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css"\n      rel="stylesheet"\n      integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9"\n      crossorigin="anonymous" />\n    <script\n      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"\n      integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm"\n      crossorigin="anonymous"\n      defer></script>\n    <title>TODO \xeb\xaa\xa9\xeb\xa1\x9d</title>\n  </head>\n  <body>\n    \n<h1>TODO LIST</h1>\n<ul>\n  \n</ul>\n<a href="/todo/new-todo">\xec\x83\x88\xeb\xa1\x9c\xec\x9a\xb4 TODO \xeb\xa7\x8c\xeb\x93\xa4\xea\xb8\xb0</a>\n\n  </body>\n</html>\n'

    def test_todo_desc_view(self):
        todo = Todo.objects.create(title="Test1", content="Test111")
        response = self.client.get(reverse("todo_description", args=(todo.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo_description.html")
        # 원하는 항목이 잘 포함되었는지 확인
        self.assertContains(response, "Test1")
        self.assertContains(response, "Test111")

    def test_create_todo_view(self):
        response = self.client.get(reverse("create_todo"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "create_todo.html")

        data = {
            "title": "Test2",
            "content": "This is my test case 2",
        }
        data2 = {
            "title": "Test2",
            "content": "This is my test case 2",
        }

        response = self.client.post(reverse("create_todo"), data)
        # ✨ 리다이렉트 했기 때문에 ➡️ 리다이렉트에 대한 응답값 : 302
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todo.objects.count(), 1)

        # ✨ DB에 잘 들어갔는지 확인
        response = self.client.post(reverse("create_todo"), data2)
        self.assertEqual(Todo.objects.count(), 2)

    def test_update_todo_view(self):
        # 화면 표시 이상 여부 확인
        todo = Todo.objects.create(title="Test", content="Test content")
        response = self.client.get(reverse("update_todo", args=(todo.pk, )))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "update_todo.html")

        # 데이터 update 수행 확인
        data = {
            "new_title": "test update",
            "new_content": "test content update",
        }

        response = self.client.post(reverse("update_todo", args=(todo.pk,)), data)

        # 전달될 데이터 반영 확인
        self.assertEqual(response.status_code, 302)

        # DB로부터 todo 내용 재갱신
        todo.refresh_from_db()
        self.assertEqual(todo.title, "test update")
        self.assertEqual(todo.content, "test content update")
        # self.assertEqual(str(Todo.objects.get(pk=todo.pk)), "test update")

    def test_delete_todo_view(self):
        todo1 = Todo.objects.create(title="Test1", content="Test content1")
        Todo.objects.create(title="Test2", content="Test content2")
        self.assertEqual(Todo.objects.count(), 2)

        data = {
            "todo_id" : f"{todo1.pk}"
        }

        response = self.client.post(reverse("delete_todo"), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(str(Todo.objects.first()), "Test2")
        self.assertEqual(str(Todo.objects.filter(pk=todo1.pk).first()), "None")