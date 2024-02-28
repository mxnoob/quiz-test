from django.shortcuts import get_object_or_404
from rest_framework import viewsets, views

from .serializers import AnswerSerializer, QuestionSerializer, GameSerializer
from core.models import Question, Game, Answer


class AnswerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows answers to be viewed
    """
    serializer_class = AnswerSerializer

    def get_queryset(self):
        return get_object_or_404(
            Question, pk=self.kwargs['question_id']
        ).answers.order_by('?')


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows questions to be viewed
    """
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return get_object_or_404(
            Game, pk=self.kwargs['game_id']
        ).questions.order_by('?')


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows games to be viewed
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
