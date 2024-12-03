from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import Conversation
from .serializers.MessageSerializer import MessageSerializer
from .schemas import list_message_docs

# Create your views here.
class MessageViewSet(ViewSet):

    @list_message_docs
    def list(self, request):
        channel_id = request.query_params.get('channel_id', None)
        try:
            conversation = Conversation.objects.get(channel_id=channel_id)
            message = conversation.messages.all()
            serializer = MessageSerializer(message, many=True)
            return Response(serializer.data)
        except Conversation.DoesNotExist:
            return Response([])



