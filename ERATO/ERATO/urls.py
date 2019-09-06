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
from loginapp import views as login_views
from swapp import views as sw_views
from clientapp import views as cl_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	path('sw/home/',sw_views.home_sw, name='home_sw'),
    path('cl/home/',cl_views.home_cl, name='home_cl'),
    path('redirect/home/',login_views.redirect_login,name='redirect'),
	path('',login_views.login, name='home'),
        path('admin/', admin.site.urls),
        path('accounts/', include('django.contrib.auth.urls')),

]

urlpatterns +=staticfiles_urlpatterns()
