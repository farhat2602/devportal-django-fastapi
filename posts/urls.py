from django.urls import path

from posts.views import QuestionsListView, QuestionCreateView, AnswerCreateView, QuestionCommentCreateView, \
    AnswerCommentCreateView

urlpatterns = [
    path('questions/', QuestionsListView.as_view()),
    path('questions/create/', QuestionCreateView.as_view()),
    path('answers/create/', AnswerCreateView.as_view()),
    path('questions/comment_create/', QuestionCommentCreateView.as_view()),
    path('answers/comment_create/', AnswerCommentCreateView.as_view()),
]
