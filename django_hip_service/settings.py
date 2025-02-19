"""
Django settings for django_hip_service project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import tomllib
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
    "https://www.alsoapp.com", # 生产环境
]
# 允许特定 HTTP 方法和请求头
CORS_ALLOW_METHODS = ["GET", "POST"]
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
    'django.contrib.staticfiles',  # 静态文件查看
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
    "cda",
    "evaluation",
    "DockerCMD",
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
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
# 这个配置定义了静态文件应用在启用 FileSystemFinder 查找器时将穿越的额外位置, 不能包含 STATIC_ROOT路径
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '/temp')
]

# 多媒体文件
MEDIA_URL = os.getenv("APP_MEDIA_URL", 'media/')
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_URL)

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

##########################################################################################
# 配置 loguru（可选）
logger.add("logs/django.log", level="INFO", rotation="10 MB", compression="zip", retention="8 days")
logger.level("INFO")  # 设置全局日志级别
##########################################################################################


SITE_ID = int(os.getenv('AP_SITE_ID', 2024))

# 以下为本地页面优化调试时开启
if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
    INTERNAL_IPS = [
        '127.0.0.1',
        'localhost'
    ]

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
