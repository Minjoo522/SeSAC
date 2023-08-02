from django.db import models

# Choices, Qestions(question(날짜, 시간)의 pk를 choice(choice, votes-count 올라가게)에서 fk로 사용)

class Question(models.Model):
    question = models.CharField(max_length=200, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200, blank=False)
    votes = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.choice