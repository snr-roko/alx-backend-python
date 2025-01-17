from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, pre_save
from .models import Message, Notification, MessageHistory 
from django.contrib.auth.models import User  

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(message=instance)

@receiver(pre_save, sender=Message)
def add_message_history(sender, instance, created, **kwargs):
    MessageHistory.objects.create(
        message_id = instance.message_id,
        content = instance.content,
        edited_by = instance.sender
    )

@receiver(post_delete, sender=User)
def delete_messages_notifications_history(sender, instance, created, **kwargs):
    Message.objects.delete(sender=instance)
    Message.objects.delete(receiver=instance)
    Notification.objects.delete()