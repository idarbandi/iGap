from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from account.views import (AccountViewSet, JWTCookieTokenObtainPairView,
                           JWTCookieTokenRefreshView, LogOutAPIView,
                           RegisterView)
from server.views import CategoryListView, ServerListView
from webchat.consumer import WebChatConsumer
from webchat.views import MessageViewSet

router = DefaultRouter()
router.register(r"server", ServerListView, basename="server-list")
router.register("category", CategoryListView, basename="category-list")
router.register("messages", MessageViewSet, basename="message-list")
router.register("users", AccountViewSet, basename="account-list")
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/docs/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/schema/ui/", SpectacularSwaggerView.as_view()),
    path(
        "api/",
        include(
            [
                path("", include(router.urls)),
            ]
        ),
    ),
    path("api/logout/", LogOutAPIView.as_view(), name="logout"),
    path("api/register/", RegisterView.as_view(), name="register"),
    path(
        "api/token/", JWTCookieTokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/", JWTCookieTokenRefreshView.as_view(), name="token_refresh"
    ),
]  # + router.urls

websocket_urlpatterns = [
    path("<str:serverId>/<str:channelId>", WebChatConsumer.as_asgi())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
