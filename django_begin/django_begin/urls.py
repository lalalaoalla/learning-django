"""
URL configuration for django_begin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.auth import views as auth_views

admin.autodiscover()#типа строчка для того, чтобы мы смогли добавлять наши таблицы

urlpatterns = [
    path("admin/", admin.site.urls),
    path('index/',include('index.urls')),#то есть, в папке индекс лежит наш файл urls, то есть следующие url смотри там
    path('catalog/',include('catalog.urls')),
    path('login/',include('login.urls')),
    path('registr/',include('registr.urls')),
    path('orders/',include('orders.urls')),
    path('my_profile/',include('my_profile.urls')),
]  \
+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
