######################################################################
#                             iGap Project                           #
######################################################################

"""
Module: server_serializer
Description: This module contains the ServerSerializer class for serializing
             Server objects, with additional fields and custom representation.
Author: idarbandi
Date: 04 December 2024
Contact: darbandidr99@gmail.com
Github: https://github.com/idarbandi
"""

from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from server.models import Server
from server.serializers import category, channel, server


class ServerSerializer(serializers.ModelSerializer):
    """
    Serializer class for Server objects.

    Attributes:
        num_members (SerializerMethodField): A custom field to get the number of members.
        category (StringRelatedField): A field to represent the category as a string.

    Meta:
        model (Server): The model that is being serialized.
        exclude (list): List of fields to exclude from the serialization.
    """
    num_members = serializers.SerializerMethodField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Server
        exclude = ["member", ]

    @extend_schema_field(serializers.IntegerField())
    def get_num_members(self, obj):
        """
        Custom method to get the number of members.

        Args:
            obj (Server): The server object being serialized.

        Returns:
            int: The number of members if the attribute exists, otherwise None.
        """
        if hasattr(obj, "num_members"):
            return obj.num_members
        return None

    def to_representation(self, instance):
        """
        Custom representation of the server instance.

        Args:
            instance (Server): The server object being serialized.

        Returns:
            dict: The serialized data representation of the server object.
        """
        data = super().to_representation(instance)
        num_members = self.context.get("num_members")
        if not num_members:
            data.pop("num_members", None)
        return data
