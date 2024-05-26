from django.contrib import admin

from .forms import GameForm, QuestionForm
from .models import Answer, Game, Question


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'correct_answer')
    list_editable = ('correct_answer',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    filter_horizontal = ('answers',)
    form = QuestionForm

    class Meta:
        model = Question


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    filter_horizontal = ('questions',)
    form = GameForm

    class Meta:
        model = Game
