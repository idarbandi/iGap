from django.db.models import Count
from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import Category, Server
from .schema import server_list_docs
from .serializers.category import CategoryListSerializer
from .serializers.server import ServerSerializer


class ServerListView(ViewSet):
    queryset = Server.objects.all()

    # permission_classes = (permissions.IsAuthenticated,)
    @server_list_docs
    def list(self, request):
        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user") == "true"
        by_serverid = request.query_params.get("by_serverid")
        with_num_members = request.query_params.get(
            "with_num_members") == "true"

        if category:
            self.queryset = self.queryset.filter(category__name=category)

        if by_user:
            if not request.user.is_authenticated:
                raise AuthenticationFailed()
            user_id = request.user.id
            self.queryset = self.queryset.filter(member=user_id)

        if with_num_members:
            self.queryset = self.queryset.annotate(num_members=Count("member"))

        if by_serverid:
            #     if not request.user.is_authenticated:
            #         raise AuthenticationFailed()
            try:
                self.queryset = self.queryset.filter(id=by_serverid)
                if not self.queryset.exists():
                    raise ValidationError(
                        detail=f"server id: {by_serverid} not found")
            except ValueError:
                raise ValidationError(detail="server value error")

        if qty:
            self.queryset = self.queryset[: int(qty)]

        serializer = ServerSerializer(
            self.queryset, many=True, context={"num_members": with_num_members}
        )
        return Response(serializer.data)


class CategoryListView(ViewSet):
    queryset = Category.objects.all()

    @extend_schema(responses=CategoryListSerializer)
    def list(self, request):
        serializer = CategoryListSerializer(self.queryset, many=True)
        return Response(serializer.data)
