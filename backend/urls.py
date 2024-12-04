"""
███████╗ ██████╗  █████╗ ██████╗     ██╗██╗   ██╗ █████╗ ██████╗ 
██╔════╝██╔════╝ ██╔══██╗██╔══██╗    ██║██║   ██║██╔══██╗██╔══██╗
███████╗██║  ███╗███████║██████╔╝    ██║██║   ██║███████║██████╔╝
╚════██║██║   ██║██╔══██║██╔═══╝     ██║██║   ██║██╔══██║██╔═══╝ 
███████║╚██████╔╝██║  ██║██║         ██║╚██████╔╝██║  ██║██║     
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝         ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     
"""

"""
این تنظیمات اصلی برنامه Django به نام iGap است.
این کامنت‌ها و داک‌استرینگ‌ها توسط Idarbandi اضافه شده‌اند.
برای پشتیبانی بیشتر لطفاً با من تماس بگیرید: darbandidr99@gmail.com
GitHub: https://github.com/idarbandi/
"""

from webchat.views import MessageViewSet
from webchat.consumer import WebChatConsumer
from server.views import CategoryListView, ServerListView
from account.views import (AccountViewSet, JWTCookieTokenObtainPairView,
                           JWTCookieTokenRefreshView, LogOutAPIView,
                           RegisterView)
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


# ساخت روتر پیش‌فرض
router = DefaultRouter()
router.register(r"server", ServerListView, basename="server-list")
router.register("category", CategoryListView, basename="category-list")
router.register("messages", MessageViewSet, basename="message-list")
router.register("users", AccountViewSet, basename="account-list")

urlpatterns = [
    path("admin/", admin.site.urls),  # مسیر پنل مدیریت
    path("api/docs/schema/", SpectacularAPIView.as_view(),
         name="schema"),  # مستندسازی API
    # رابط کاربری Swagger
    path("api/docs/schema/ui/", SpectacularSwaggerView.as_view()),
    path(
        "api/",
        include(
            [
                # اضافه کردن مسیرهای API به روتر
                path("", include(router.urls)),
            ]
        ),
    ),
    path("api/logout/", LogOutAPIView.as_view(), name="logout"),  # مسیر خروج
    path("api/register/", RegisterView.as_view(),
         name="register"),  # مسیر ثبت نام
    path(
        # مسیر دریافت توکن JWT
        "api/token/", JWTCookieTokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        # مسیر تازه‌سازی توکن JWT
        "api/token/refresh/", JWTCookieTokenRefreshView.as_view(), name="token_refresh"
    ),
]

# مسیرهای WebSocket
websocket_urlpatterns = [
    path("<str:serverId>/<str:channelId>", WebChatConsumer.as_asgi())
]

# اضافه کردن مسیرهای استاتیک در حالت دیباگ
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
