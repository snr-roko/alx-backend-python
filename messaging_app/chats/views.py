from django.shortcuts import render
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from rest_framework.viewsets import ModelViewSet

class ConversationViewSet(ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
