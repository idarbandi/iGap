from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.response import Response

from .models import Server
from .schema import server_list_docs
from .serializer import ServerSerializer


class ServerListViewSet(viewsets.ViewSet):
    """
    یک ویوست برای فهرست و فیلتر کردن اشیاء سرور.

    صفات:
        queryset (QuerySet): queryset اولیه برای بازیابی تمام اشیاء سرور.

    متدها:
        list(request): پردازش درخواست‌های GET برای فهرست کردن سرورها با فیلترهای اختیاری.
    """

    # Set the initial queryset to retrieve all Server objects
    queryset = Server.objects.all()

    @server_list_docs
    def list(self, request):
        """
        پردازش درخواست‌های GET برای فهرست کردن سرورها.

        آرگومان‌ها:
            request (HttpRequest): شیء درخواست که شامل پارامترهای query است.

        ارور‌ها:
            AuthenticationFailed: اگر کاربر احراز هویت نشده باشد و تلاش به فیلتر کردن بر اساس شناسه کاربر یا سرور کند.
            ValidationError: اگر شناسه سرور ارائه شده معتبر نباشد یا هیچ سروری با آن شناسه یافت نشود.

        بازگشتی‌ها:
            Response: یک شیء پاسخ که شامل داده‌های سریال شده از queryset سرور فیلتر شده است.
        """
        # Extract query parameters from the request
        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user") == "true"
        by_server_id = request.query_params.get("by_server_id")
        with_num_members = request.query_params.get("with_num_members") == "true"

        # Filter queryset by category if provided
        if category:
            self.queryset = self.queryset.filter(category__name=category)

        # Filter queryset by the authenticated user if requested
        if by_user and request.user.is_authenticated:
            user_id = request.user.id
            self.queryset = self.queryset.filter(member=user_id)
        else:
            raise AuthenticationFailed()

        # Limit the number of results if quantity is specified
        if qty:
            self.queryset = self.queryset[: int(qty)]

        if with_num_members:
            self.queryset = self.queryset.annotate(num_members=Count("member"))

        # Filter queryset by server ID if provided and handle potential errors
        if by_server_id:
            # Ensure user is authenticated if filtering by server ID or user
            if not request.user.is_authenticated:
                raise AuthenticationFailed()

            try:
                self.queryset = self.queryset.filter(id=by_server_id)
                if not self.queryset.exists():
                    raise ValidationError(
                        detail=f"Server With Id {by_server_id} not found"
                    )
            except ValueError:
                raise ValidationError(detail="Server Value Error")

        # Serialize the filtered queryset and return the data in the response
        serializer = ServerSerializer(
            self.queryset, many=True, context={"num_members": with_num_members}
        )
        return Response(serializer.data)
