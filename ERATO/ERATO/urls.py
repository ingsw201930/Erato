"""ERATO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from app_sessions import views as sessions_views
from app_sw import views as sw_views
from app_client import views as cl_views
from app_date import views as date_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	path('sw/home/',sw_views.home_sw, name='home_sw'),
    path('cl/home/',cl_views.home_cl, name='home_cl'),
    path('redirect/home/',sessions_views.redirect_login,name='redirect'),
    path('createQR/<int:date_id>',date_views.createQR),
    path('QRcheck/<str:code>',date_views.checkQR),
        path('admin/', admin.site.urls),
        path('', include('django.contrib.auth.urls')),

]

urlpatterns +=staticfiles_urlpatterns()
