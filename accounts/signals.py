from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import CustomUser, Profile


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created and instance.is_company == False:
        Profile.objects.create(user=instance)

