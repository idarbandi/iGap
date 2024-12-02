from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from server.models import Server

from server.serializers.channel import ChannelSerializer

class ServerSerializer(serializers.ModelSerializer):
    num_members = serializers.SerializerMethodField()
    channel_server = ChannelSerializer(many=True)
    category = serializers.StringRelatedField()
    class Meta:
        model = Server
        exclude = ["member", ]

    @extend_schema_field(serializers.IntegerField())
    def get_num_members(self, obj):
        if hasattr(obj, "num_members"):
            return obj.num_members
        return None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        num_members = self.context.get("num_members")
        if not num_members:
            data.pop("num_members", None)
        return data