from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid4, db_index=True)
    sender = models.ForeignKey(User, related_name='messages_sent', on_delete=models.PROTECT)
    receiver = models.ForeignKey(User, related_name='messages_received', on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

class Notification(models.Model):
    notification_id = models.UUIDField(primary_key=True, default=uuid4, db_index=True)
    message = models.ForeignKey(Message, related_name='notifications', on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)