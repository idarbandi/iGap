######################################################################
#                             iGap Project                           #
######################################################################

"""
Module: server_filter
Description: This module defines the ServerFilter class for filtering 
             Server objects based on specific criteria.
Author: idarbandi
Date: 04 December 2024
Contact: darbandidr99@gmail.com
Github: https://github.com/idarbandi
"""

from django.db.models import Count
from django_filters import (BooleanFilter, CharFilter, FilterSet, NumberFilter,
                            NumericRangeFilter)
from rest_framework.exceptions import ValidationError

from server.models import Server


class ServerFilter(FilterSet):
    """
    A filter class for filtering Server objects based on specific criteria.

    Attributes:
        by_serverid (NumberFilter): Filters servers by their ID.

    Meta:
        model (Server): The model to be filtered.
        fields (dict): Dictionary of fields to be filtered and their lookup expressions.
    """
    by_serverid = NumberFilter(field_name="id")

    class Meta:
        model = Server
        fields = {
            "category__name": ["exact"],
            "member": ["icontains"],
        }
