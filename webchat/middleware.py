######################################################################
#                             iGap Project                           #
######################################################################

"""
Module: custom_middleware
Description: This module contains a custom JWT authentication middleware for the iGap project,
             which processes WebSocket connections and authenticates users using JWT tokens.
Author: idarbandi
Date: 04 December 2024
Contact: darbandidr99@gmail.com
Github: https://github.com/idarbandi
"""

import jwt
from channels.db import database_sync_to_async
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser


@database_sync_to_async
def get_user(scope):
    """
    Retrieves the user based on the JWT token provided in the scope.

    Args:
        scope (dict): The scope dictionary containing connection information.

    Returns:
        User or AnonymousUser: The authenticated user object or AnonymousUser if authentication fails.
    """
    token = scope["token"]
    model = get_user_model()

    try:
        if token:
            user_id = jwt.decode(token, settings.SECRET_KEY,
                                 algorithms=["HS256"])["user_id"]
            return model.objects.get(id=user_id)
        else:
            return AnonymousUser()
    except (jwt.exceptions.DecodeError, model.DoesNotExist):
        return AnonymousUser()


class JWTAuthMiddleWare:
    """
    Custom middleware for JWT authentication in WebSocket connections.

    This middleware extracts the JWT token from the cookies in the WebSocket scope,
    authenticates the user, and attaches the user object to the scope.
    """

    def __init__(self, app):
        """
        Initializes the middleware with the ASGI application.

        Args:
            app (ASGI application): The ASGI application instance.
        """
        self.app = app

    async def __call__(self, scope, receive, send):
        """
        Processes the WebSocket connection and performs JWT authentication.

        Args:
            scope (dict): The scope dictionary containing connection information.
            receive (function): The function to receive WebSocket messages.
            send (function): The function to send WebSocket messages.
        """
        # Extract cookies from the headers
        headers_dict = dict(scope["headers"])
        cookies_str = headers_dict.get(b"cookie", b"").decode()
        cookies = {cookie.split("=")[0]: cookie.split("=")[1]
                   for cookie in cookies_str.split("; ")}
        access_token = cookies.get("access_token")

        # Add the JWT token and authenticated user to the scope
        scope["token"] = access_token
        scope["user"] = await get_user(scope)

        # Call the next middleware or application
        return await self.app(scope, receive, send)
