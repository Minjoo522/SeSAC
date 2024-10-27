from django.test import TestCase
from django.urls import reverse
from .models import Question, Choice

class PollsModelTests(TestCase):
    def test_str_representation_question(self):
        question = Question.objects.create(question="Test1")
        self.assertEqual(str(question), "Test1")
    
    def test_str_representation_choice(self):
        question = Question.objects.create(question="Test1")
        choice1 = Choice.objects.create(question=question, choice="Test choice 1")
        choice2 = Choice.objects.create(question=question, choice="Test choice 2")
        choice3 = Choice.objects.create(question=question, choice="Test choice 3")
        self.assertEqual(str(choice1), "Test choice 1")
        self.assertEqual(str(choice2), "Test choice 2")
        self.assertEqual(str(choice3), "Test choice 3")

class PollsViewTests(TestCase):
    def test_polls_list_view(self):
        response = self.client.get(reverse("polls_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "polls/polls_list.html")

    def test_polls_choice(self):
        # 데이터 생성
        question = Question.objects.create(question="Test1")
        choice1 = Choice.objects.create(question=question, choice="Test choice 1")
        choice2 = Choice.objects.create(question=question, choice="Test choice 2")
        choice3 = Choice.objects.create(question=question, choice="Test choice 3")

        # get 일 때, 화면 표시
        response = self.client.get(reverse("polls_choice", args=(question.pk, )))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "polls/polls_choice.html")

        self.assertContains(response, "Test choice 1")
        self.assertContains(response, "Test choice 2")
        self.assertContains(response, "Test choice 3")

        # post 일 때, 동작
        data1 = {
            "choice" : f"{choice1.pk}"
        }

        data2 = {
            "choice" : f"{choice2.pk}"
        }

        data3 = {
            "choice" : f"{choice3.pk}"
        }

        # choice1 선택시
        response = self.client.post(reverse("polls_choice", args=(question.pk, )), data1)
        self.assertEqual(response.status_code, 302)

        choice1.refresh_from_db()
        self.assertEqual(choice1.votes, 1)
        choice2.refresh_from_db()
        self.assertEqual(choice2.votes, 0)
        self.assertEqual(choice3.votes, 0)
        self.assertRedirects(response, reverse("polls_result", args=(question.pk, choice1.pk)), status_code=302, target_status_code=200)
        
        # choice2 선택시
        response = self.client.post(reverse("polls_choice", args=(question.pk, )), data2)
        self.assertEqual(response.status_code, 302)

        choice2.refresh_from_db()
        self.assertEqual(choice2.votes, 1)
        self.assertRedirects(response, reverse("polls_result", args=(question.pk, choice2.pk)), status_code=302, target_status_code=200)

        # choice3 선택시
        response = self.client.post(reverse("polls_choice", args=(question.pk, )), data3)
        self.assertEqual(response.status_code, 302)

        choice3.refresh_from_db()
        self.assertEqual(choice3.votes, 1)
        self.assertRedirects(response, reverse("polls_result", args=(question.pk, choice3.pk)), status_code=302, target_status_code=200)

    def test_polls_result_view(self):
        # 데이터 생성
        question = Question.objects.create(question="Test1")
        choice1 = Choice.objects.create(question=question, choice="Test choice 1", votes=1)
        choice2 = Choice.objects.create(question=question, choice="Test choice 2", votes=2)
        choice3 = Choice.objects.create(question=question, choice="Test choice 3", votes=3)

        # get일 때, 화면 표시
        response = self.client.get(reverse("polls_result", args=(question.pk, choice1.pk)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "polls/polls_result.html")

        # post일 때, 동작
        response = self.client.post(reverse("polls_result", args=(question.pk, choice1.pk)))
        self.assertEqual(response.status_code, 302)
        choice1.refresh_from_db()
        self.assertEqual(choice1.votes, 0)
        self.assertEqual(choice2.votes, 2)
        self.assertEqual(choice3.votes, 3)
        self.assertRedirects(response, reverse("polls_choice", args=(question.pk, )), status_code=302, target_status_code=200)