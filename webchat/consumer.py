######################################################################
#                             iGap Project                           #
######################################################################

"""
Module: websocket_consumer
Description: This module defines the WebChatConsumer class for handling WebSocket
             connections for chat functionality in the iGap project.
Author: idarbandi
Date: 04 December 2024
Contact: darbandidr99@gmail.com
Github: https://github.com/idarbandi
"""

from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer
from django.contrib.auth import get_user_model

from .models import Conversation, Message

User = get_user_model()


class WebChatConsumer(JsonWebsocketConsumer):
    """
    WebSocket consumer class to handle real-time chat functionality.

    Attributes:
        channel_id (str): The ID of the chat channel.
        user (User): The user connected to the WebSocket.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.channel_id = None
        self.user = None

    def connect(self):
        """
        Method called when a WebSocket connection is established.

        Authenticates the user and joins them to the chat channel.
        """
        self.user = self.scope["user"]
        self.accept()
        if not self.user.is_authenticated:
            # Close connection if user is not authenticated
            self.close(code=4001)

        self.channel_id = self.scope["url_route"]["kwargs"]["channelId"]

        # Temporary line for testing purposes
        self.user = User.objects.get(id=1)

        # Add the user to the chat channel group
        async_to_sync(self.channel_layer.group_add)(
            self.channel_id, self.channel_name)

    def receive_json(self, content):
        """
        Method called when a JSON message is received.

        Creates a new message in the conversation and sends it to the channel group.

        Args:
            content (dict): The JSON message content.
        """
        channel_id = self.channel_id
        sender = self.user
        message = content["message"]

        # Retrieve or create a conversation for the channel
        conversation, created = Conversation.objects.get_or_create(
            channel_id=channel_id)

        # Create a new message
        new_message = Message.objects.create(
            conversation=conversation, sender=sender, content=message)

        # Send the new message to the channel group
        async_to_sync(self.channel_layer.group_send)(
            self.channel_id,
            {
                "type": "chat.message",
                "new_message": {
                    "id": new_message.id,
                    "sender": new_message.sender.username,
                    "content": new_message.content,
                    "timestamp": new_message.timestamp.isoformat(),
                },
            },
        )

    def chat_message(self, event):
        """
        Method to handle sending the chat message to the WebSocket.

        Args:
            event (dict): The event data containing the new message.
        """
        self.send_json(event)

    def disconnect(self, close_code):
        """
        Method called when the WebSocket connection is closed.

        Removes the user from the chat channel group.

        Args:
            close_code (int): The close code for the WebSocket connection.
        """
        async_to_sync(self.channel_layer.group_discard)(
            self.channel_id, self.channel_name)
        super().disconnect(close_code)
