from django.db import models


class Answer(models.Model):
    text = models.TextField()
    correct_answer = models.BooleanField(default=False)

    def __str__(self):
        return ("✔ " if self.correct_answer else "❌ ") + self.text[:50]


class Question(models.Model):
    title = models.CharField(max_length=250)
    answers = models.ManyToManyField(Answer)

    def __str__(self):
        return self.title[:50]


class Game(models.Model):
    title = models.CharField(max_length=50)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.title
