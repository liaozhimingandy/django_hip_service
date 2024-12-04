"""
Django settings for django_hip_service project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import logging
import subprocess
import time
import tomllib

from django import get_version
import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

from django.contrib import admin
from django.utils.html import format_html
from loguru import logger

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# 从pyproject.toml加载应用版本号等信息
def get_version_from_pyproject():
    with open(os.path.join(BASE_DIR, "pyproject.toml"), "rb") as f:
        data = tomllib.load(f)
    # 假设版本号位于 [tool.poetry] 或 [project] 中
    return data.get("project", {}).get("version"), data.get("project", {}).get("description")


__version__, APP_NAME = get_version_from_pyproject()

# id前缀
PREFIX_ID = "esbid_"

# 从本地加载.env文件到环境变量中
_ = load_dotenv(find_dotenv())

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("APP_SECRET_KEY", 'django-insecure-&(s=fs#s3b9&=8&y_+bhzquk_1-uq)iu@=v=%+&qegp9958%e$')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.getenv("APP_DEBUG", 1))
ALLOWED_HOSTS = os.getenv("APP_DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1,openapi.esb.alsoapp.com,"
                                                      "openapi-test.esb.alsoapp.com").split(",")

CSRF_TRUSTED_ORIGINS = [f'http://{item}' for item in ALLOWED_HOSTS]
# 允许来自指定来源的跨域请求
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # 允许 Vue 开发服务器的地址
]
# 允许特定 HTTP 方法和请求头
CORS_ALLOW_METHODS = ["GET", "POST", "PUT", "PATCH", "OPTIONS"]
# Application definition
# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.admindocs",  # 供生成文档使用
    "django.contrib.sites",  # 站点使用
]

THIRD_PARTY_APPS = [
    "django_json_widget",
    'graphene_django',
]

LOCAL_APPS = [
    "hipmessageservice",
    "cdr",
    "evaluation"
    # Your stuff: custom apps go here
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django.contrib.admindocs.middleware.XViewMiddleware",  # 供生成文档标签使用
]

ROOT_URLCONF = 'django_hip_service.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_hip_service.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": os.getenv("APP_DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.getenv("APP_DB_NAME", BASE_DIR / "cdr.db"),
        "USER": os.getenv("APP_DB_USER", ""),
        "PASSWORD": os.getenv("APP_DB_PASSWORD", ""),
        "HOST": os.getenv("APP_DB_HOST", ""),
        "PORT": os.getenv("APP_DB_PORT", ""),
    },
    "test": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / os.getenv("APP_DB_NAME", "cdr-test.db")
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = os.getenv('APP_LANGUAGE_CODE', 'zh-hans')
TIME_ZONE = os.getenv('APP_TIME_ZONE', 'Asia/Shanghai')
USE_I18N = True
USE_TZ = True

# 静态方式 (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = os.getenv("APP_STATIC_URL", 'static/')

# Default primary key field type
# https://docs.djangoproject.com/zh-hans/5.0/howto/static-files/
# python manage.py collectstatic 收集文件到下面文件文件夹里
STATIC_ROOT = os.path.join(BASE_DIR, "static")
# STATICFILES_DIRS = [BASE_DIR / "static", ]

# 多媒体文件
MEDIA_URL = os.getenv("APP_MEDIA_URL", 'media/')
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_URL)

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ######################### 日志配置开始 ######################### #
# 参考链接: https://www.jb51.net/article/260114.htm

# BASE_LOG_DIR = os.path.join(BASE_DIR, "logs")
# if not os.path.exists(BASE_LOG_DIR):
#     os.makedirs(BASE_LOG_DIR)
#
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '{asctime:<19}|{levelname:<10}|{process:d}:{thread:d}:{module}:{funcName}:{lineno}|{message}',
#             'style': '{',
#             "datefmt": "%Y-%m-%d %H:%M:%S",
#         },
#         'simple': {
#             'format': '{asctime:<19}|{levelname:<10}|{message}',
#             'style': '{',
#             "datefmt": "%Y-%m-%d %H:%M:%S",
#         },
#         "default": {
#             "format": '{asctime:<19}|{name}|{levelname:<10}|{pathname}:{lineno}|{module}:{funcName}|{message}',
#             'style': '{',
#             "datefmt": "%Y-%m-%d %H:%M:%S"
#         },
#     },
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse',
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': logging.INFO,
#             'class': 'logging.StreamHandler',
#             'formatter': 'default'
#         },
#         'file': {
#             'level': logging.INFO,
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'filename': os.path.join(BASE_DIR, f"logs/django-{time.strftime('%Y-%m-%d')}.log"),
#             'filters': ['require_debug_true', ],
#             "when": 'D',  # 时间单位： M, H, D， W0(周一), W6(周日)
#             "interval": 1,
#             "backupCount": 7,  # 备份数量
#             "formatter": "verbose",  # 日志格式
#             "encoding": "utf-8"
#         },
#         "request": {
#             'level': logging.DEBUG,
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, f"logs/{time.strftime('%Y-%m-%d')}-request.log"),
#             'filters': ['require_debug_true', "require_debug_false"],
#             'formatter': 'default'
#         },
#         "server": {
#             'level': logging.DEBUG,
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, f"logs/{time.strftime('%Y-%m-%d')}-server.log"),
#             'filters': ['require_debug_true', ],
#             'formatter': 'default'
#         },
#         "db_backends": {
#             'level': logging.DEBUG,
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, f"logs/{time.strftime('%Y-%m-%d')}-db_backends.log"),
#             'filters': ['require_debug_true', ],
#             'formatter': 'default'
#         },
#         "autoreload": {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, f"logs/{time.strftime('%Y-%m-%d')}-autoreload.log"),
#             'formatter': 'default'
#         },
#         # 电子邮件发给管理员
#         "mail_admins": {
#             "level": logging.ERROR,
#             "class": "django.utils.log.AdminEmailHandler",
#             "filters": ["require_debug_false"],
#         }
#     },
#     "root": {
#             "handlers": ["console"],
#             "level": "WARNING",
#         },
#     'loggers': {
#         # 应用中自定义日志记录器
#         'mylogger': {
#             'level': os.getenv("DJANGO_LOG_LEVEL", logging.DEBUG),
#             'handlers': ['console', 'file'],
#             'propagate': True,
#         },
#         # django这个日志记录器（logger）是用来记录Django框架本身生成的日志消息的
#         "django": {
#             "level": os.getenv("DJANGO_LOG_LEVEL", logging.DEBUG),
#             "handlers": ["console", "file"],
#             'propagate': False,  # 阻止Django日志传播到根记录器
#         },
#         "django.request": {
#             "level": os.getenv("DJANGO_LOG_LEVEL", logging.DEBUG),
#             "handlers": ["request", "console"],
#             'propagate': False,
#         },
#         "django.server": {
#             "level": os.getenv("DJANGO_LOG_LEVEL", logging.DEBUG),
#             "handlers": ["server"],
#             'propagate': False,
#         },
#         "django.db.backends": {
#             "level": os.getenv("DJANGO_LOG_LEVEL", logging.DEBUG),
#             "handlers": ["db_backends"],
#             'propagate': False,
#         },
#         "django.utils.autoreload": {
#             "level": os.getenv("DJANGO_LOG_LEVEL", logging.DEBUG),
#             "handlers": ["autoreload"],
#             'propagate': False,
#         }
#     }
# }
# e.g. logger = logging.getLogger("mylogger")
# ######################### 日志配置结束 ######################### #

##########################################################################################
# 配置 loguru（可选）
logger.add("logs/django.log", level="INFO", rotation="10 MB", compression="zip", retention="8 days")
logger.level("INFO")  # 设置全局日志级别
##########################################################################################


SITE_ID = int(os.getenv('AP_SITE_ID', 2024))

# 以下为本地页面优化调试时开启
# if DEBUG:
#     INSTALLED_APPS.append('debug_toolbar')
#     MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
#     INTERNAL_IPS = [
#         '127.0.0.1',
#         'localhost'
#     ]

admin.AdminSite.site_title = format(f"{APP_NAME}")
admin.AdminSite.site_header = format_html(f'{APP_NAME} | <span style="color:white"> {__version__}</span>')
# 患者注册,恺恩泰empi接口
EMPI_API_URL = os.getenv('EMPI_API_URL', 'http://172.16.33.181:8253/webservice/IndexRegisterService.asmx')
# 上传给市互认平台使用
HOSPITAL_KEY = os.getenv('HOSPITAL_KEY', 'tGuWgUr8PaS3dl7m')
HOSPITAL_ID = os.getenv('HOSPITAL_ID', 'ytlyyy_001')
HOSPITAL_CODE = os.getenv('HOSPITAL_CODE', '12360000491015900T')
IS_SAVE_TO_DB = os.getenv('IS_SAVE_TO_DB', 1)
# 单体应用数据库层面创建外键约束
IS_DB_CONSTRAINT = os.getenv('IS_DB_CONSTRAINT', 1)

##########################################################################################
# GraphQL 配置
GRAPHENE = {
    'SCHEMA': 'cdr.schema.schema',  # 指向你的 schema 文件
}
##########################################################################################
