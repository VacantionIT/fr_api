from enum import Enum

from django.db import models


class QuestionType(Enum):
    TEXT = "TEXT"
    SELECT = "SELECT"
    MULTI_SELECT = "MULTI_SELECT"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class Questionnaire(models.Model):
    title = models.CharField(max_length=255, blank=False)
    # По условию не понятно какие поля обязательные, так что определем так:
    date_start = models.DateField()  # blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    q_text = models.TextField(blank=False)
    q_type = models.CharField(max_length=15, choices=QuestionType.choices(),
                              blank=False,
                              null=False)
    questionnaire = models.ForeignKey(Questionnaire,
                                      on_delete=models.CASCADE,
                                      related_name="questions"
                                      )

    def __str__(self):
        return self.q_text[:100]


class Answer(models.Model):
    user_id = models.IntegerField(blank=False, null=False)
    question = models.ForeignKey(Question, on_delete=models.PROTECT, related_name='answer', blank=False, null=False)
    answer = models.TextField(blank=False, null=False)

    def __str__(self):
        return f'{self.answer} on {self.question} from {self.user_id}'
