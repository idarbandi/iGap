from django.db.models import Count
from django_filters import (
    FilterSet,
    NumericRangeFilter,
    CharFilter,
    NumberFilter,
    BooleanFilter,
)
from rest_framework.exceptions import ValidationError

from server.models import Server


class ServerFilter(FilterSet):
    by_serverid = NumberFilter(field_name="id")
#     member_username_contains = NumberFilter(field_name="username")(
#     field_name="member__pk", lookup_expr="icontains"
# )

    class Meta:
        model = Server
        fields = {
            "category__name": ["exact"],
            "member": ["icontains"],
        }
