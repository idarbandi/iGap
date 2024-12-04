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

from dotenv import load_dotenv
from pathlib import Path
import os
from datetime import timedelta


load_dotenv()

# مسیرهای داخل پروژه را مانند این بسازید: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG")
ALLOWED_HOSTS = []

# تعریف برنامه‌ها

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # برنامه‌های خارجی
    'drf_spectacular',
    "rest_framework",
    'django_filters',
    "corsheaders",
    'rest_framework_simplejwt',
    # برنامه‌های داخلی
    "account",
    "server",
    "webchat"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"


# پایگاه داده
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# اعتبارسنجی رمز عبور
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# بین‌المللی‌سازی
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# فایل‌های استاتیک (CSS، جاوا اسکریپت، تصاویر)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = 'static/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "media/"

# نوع فیلد کلید اصلی پیش‌فرض
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "account.Account"

REST_FRAMEWORK = {
    # تنظیمات شما
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # "rest_framework.authentication.SessionAuthentication",
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        "account.authenticate.JWTCookieAuthentication"
    ],
    # 'DEFAULT_FILTER_BACKENDS': [
    #     'django_filters.rest_framework.DjangoFilterBackend',
    #     # 'rest_framework.filters.OrderingFilter',  # می‌توانید فیلترهای دیگر نیز اضافه کنید.
    # ],
}

# Metadata رابط کاربری Swagger
SPECTACULAR_SETTINGS = {
    "SWAGGER_UI_DIST": "SIDECAR",  # shorthand to use the sidecar instead
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
    # تنظیمات دیگر
}

# CORS_ALLOWED_ORIGINS = [
#     "http://127.0.0.1:5173",
#     "htts://localhost:5173"
# ]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(seconds=10),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),  # - every 30 days relogin
    # JWTCookie
    "ACCESS_TOKEN_NAME": "access_token",
    "REFRESH_TOKEN_NAME": "refresh_token",
    "JWT_COOKIE_SAMESITE": "Lax"
}
