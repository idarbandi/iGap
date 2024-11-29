from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema

from .serializer import ChannelSerializer, ServerSerializer

server_list_docs = extend_schema(responses=ServerSerializer(many=True), parameters=[
    OpenApiParameter(
        name='category',
        type=OpenApiTypes.STR,
        description='category of formats for your needs'
    ),
    OpenApiParameter(
        name='qty',
        type=OpenApiTypes.INT,
        location='openAPIParameter.QUERY',
        description='Numbers Of Servers to Retrieve'
    ),
    OpenApiParameter(
        name='by_user',
        type=OpenApiTypes.BOOL,
        location='openAPIParameter.QUERY',
        description='Filter Servers By The Current Authenticated Users'
    ),
    OpenApiParameter(
        name='with_num_members',
        type=OpenApiTypes.BOOL,
        location='openAPIParameter.QUERY',
        description='Include The Number Of Member for each server in the response'
    ),
    OpenApiParameter(
        name='by_server_id',
        type=OpenApiTypes.INT,
        description='include server by server id'
    )
]
)
