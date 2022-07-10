from django.contrib.auth import get_user_model
from django.db import models

from rooms.models import Teams

User = get_user_model()


CHOICE = [
    ('Open', 'Open'),
    ('Close', 'Close')
]


class Questions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_question')
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='team_question')
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(choices=CHOICE, max_length=24)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Answers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_answer')
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_help = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class QuestionComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_question_comment')
    comment = models.ForeignKey('self', on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class AnswerComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_answer_comment')
    comment = models.ForeignKey('self', on_delete=models.CASCADE)
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

