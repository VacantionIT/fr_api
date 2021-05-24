import datetime

from django.db.models import Q
from rest_framework import authentication, permissions, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *


class AuthView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        return Response({'detail': 'Ok'}, status=status.HTTP_200_OK)


class QuestionnaireCreateView(generics.CreateAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    permission_classes = [permissions.IsAdminUser]


class QuestionnaireActiveListView(generics.ListAPIView):
    # queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer

    def get_queryset(self):
        queryset = Questionnaire.objects.filter(Q(date_start__lte=datetime.datetime.now()) &
                                                Q(Q(date_end__gte=datetime.datetime.now()) | Q(date_end__isnull=True)))
        return queryset


class QuestionnaireUpdateView(generics.UpdateAPIView):
    serializer_class = QuestionnaireUpdateSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        queryset = Questionnaire.objects.filter(id=self.kwargs.get('pk'))
        return queryset


class QuestionnaireDeleteView(generics.DestroyAPIView):
    # queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        queryset = Questionnaire.objects.filter(id=self.kwargs.get('pk'))
        return queryset


class QuestionCreateView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAdminUser]


class QuestionUpdateView(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        queryset = Question.objects.filter(id=self.kwargs.get('pk'))
        return queryset


class QuestionDeleteView(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        queryset = Question.objects.filter(id=self.kwargs.get('pk'))
        return queryset


class AnswerCreateView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerCreateSerializer


class ResultQuestionnaireListView(generics.ListAPIView):
    serializer_class = FinishedQuestionnaireUserSerializer

    def get_queryset(self):
        pk_key = self.kwargs.get('pk')
        queryset = Questionnaire.objects.filter(questions__answer__user_id=pk_key).distinct()
        return queryset

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        for data in response.data:
            data.update({'user_id': self.kwargs['pk']})
        return response
