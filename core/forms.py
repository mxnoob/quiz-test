from django import forms

from .models import Game, Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'answers']

    def clean(self):
        answers = self.cleaned_data['answers']
        if answers_count := answers.count() != 4:
            raise forms.ValidationError(
                f'Answers count must be 4. Got {answers_count}'
            )
        if (
            len(list(filter(lambda answer: answer.correct_answer, answers)))
            != 1
        ):
            raise forms.ValidationError('Only 1 answer must be correct')
        return self.cleaned_data


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'questions']

    def clean(self):
        questions_count = self.cleaned_data['questions'].count()
        if questions_count != 10:
            raise forms.ValidationError(
                f'Game must have 10 questions. '
                f'You have {questions_count} questions.'
            )
        return self.cleaned_data
