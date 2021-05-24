from rest_framework import serializers
from .models import *


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = '__all__'


class QuestionnaireUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ['id', 'title', 'date_end', 'description']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class AnswersUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'question', 'answer']


class FinishedQuestionnaireUserSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()

    def get_answers(self, obj):
        return []

    def get_user_id(self, obj):
        return self.context['view'].kwargs.get('pk')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        user_id = ret.get('user_id')
        answers = Answer.objects.filter(user_id=user_id)
        s_answers = AnswersUserSerializer(answers, many=True)
        ret['answers'] = s_answers.data
        return ret

    class Meta:
        model = Questionnaire
        fields = ['id', 'title', 'answers', 'user_id']
