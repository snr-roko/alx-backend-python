from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .models import Message, Notification

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(message=instance)