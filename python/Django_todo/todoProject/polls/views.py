from django.shortcuts import render, redirect
from .models import Question, Choice

def polls_list(request):
    questions = Question.objects.all()
    return render(request, "polls/polls_list.html", {"questions": questions})

def polls_choice(request, question_id):
    choices = Choice.objects.filter(question=question_id).all()
    if request.method == "POST":
      selected_choice = request.POST["choice"]
      choice = Choice.objects.get(pk=selected_choice)
      choice.votes += 1
      choice.save()
      return redirect("polls_result", question_id, choice.pk)
    return render(request, "polls/polls_choice.html", {"choices": choices})

def polls_result(request, question_id, choice_id):
    choices = Choice.objects.filter(question=question_id).all()
    if request.method == "POST":
      choice = Choice.objects.get(pk=choice_id)
      choice.votes -= 1
      choice.save()
      return redirect("polls_choice", question_id)
    return render(request, "polls/polls_result.html", {"choices": choices})