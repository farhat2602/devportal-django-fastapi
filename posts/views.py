from rest_framework import generics

from posts.models import Questions
from posts.serializers import QuestionsSerializer, AnswerSerializer, QuestionCommentSerializer, \
    AnswerCommentSerializer


class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionsSerializer


class QuestionsListView(generics.ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class AnswerCreateView(generics.CreateAPIView):
    serializer_class = AnswerSerializer


class QuestionCommentCreateView(generics.CreateAPIView):
    serializer_class = QuestionCommentSerializer


class AnswerCommentCreateView(generics.CreateAPIView):
    serializer_class = AnswerCommentSerializer
