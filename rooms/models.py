from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import models


User = get_user_model()


CHOICE = [
    ('Open', 'Open'),
    ('Close', 'Close')
]


class Teams(Group):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subscribes = models.ManyToManyField(User, related_name='followers', symmetrical=False)
    status = models.CharField(choices=CHOICE, max_length=24)
    avatar = models.ImageField(upload_to='teams_avatars/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    invite_code = models.IntegerField()

    def __str__(self):
        return self.name

