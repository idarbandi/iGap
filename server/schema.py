######################################################################
#                             iGap Project                           #
######################################################################

"""
Module: schema
Description: This module defines the schema for the iGap project,
             using drf_spectacular for API documentation.
Author: idarbandi
Date: 04 December 2024
Contact: darbandidr99@gmail.com
Github: https://github.com/idarbandi
"""

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema

from .serializers.server import ServerSerializer

# Define API schema for server list endpoint
server_list_docs = extend_schema(
    responses=ServerSerializer(many=True),  # Serializer for the response
    parameters=[
        OpenApiParameter(
            name="category",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            # Query parameter for server category
            description="Category of servers to retrieve",
        ),
        OpenApiParameter(
            name="qty",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            # Query parameter for the number of servers
            description="Qty of servers to retrieve",
        ),
        OpenApiParameter(
            name="by_user",
            type=OpenApiTypes.BOOL,
            location=OpenApiParameter.QUERY,
            # Query parameter for user-related servers
            description="Get servers related to this user (True/False)",
        ),
        OpenApiParameter(
            name="with_num_members",
            type=OpenApiTypes.BOOL,
            location=OpenApiParameter.QUERY,
            # Query parameter to include member count
            description="Include the number of members for each server",
        ),
        OpenApiParameter(
            name="by_serverid",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description="Filter by server ID",  # Query parameter to filter by server ID
        ),
    ]
)
