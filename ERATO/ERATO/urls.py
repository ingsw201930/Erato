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
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


from app_sessions import views as session_views
from app_sw import views as sw_views
from app_client import views as client_views
from app_date import views as date_views
from app_transactions import views as ts_views

urlpatterns = [
    path('admin/', admin.site.urls),

#   SESSIONS
    path('',session_views.main_,name='main'),
    path('accounts/login/?next=/sessions_managing_login/',session_views.login_managing,name='login'),
    path('sessions_managing_login/',session_views.login_managing,name='login'),
    path('c/login/', auth_views.LoginView.as_view(template_name='login_c/login.html') , name="login_c"),
    path('s/login/', auth_views.LoginView.as_view(template_name='login_s/login.html') , name="login_s"),
    path('logout/', session_views.logout_managing),
    path('authenticate_user/', session_views.authenticate_user),
    path('s/signupform/',sw_views.signupform,name="signup_s"),
    path('c/signupform/',client_views.signupform,name="signup_c"),
    path('s/signup/',sw_views.signup,name="signup_s"),
    path('c/signup/',client_views.signup,name="signup_c"),

#   Sw functionalities
    path('s/home/', sw_views.home_s , name="home_s"),
    path('s/service_add_request/', sw_views.service_add_form , name="service_add"),
    path('s/service_add_request/service_adding_service/', sw_views.service_add , name="service_add"),
    path('s/service_del/<int:service_id>', sw_views.service_del , name="service_del"),
    path('s/account_del/<int:sw_id>', sw_views.account_del , name="account_del"),
    path('s/edit_profile', sw_views.edit_profile , name="service_del"),
    path('s/upload_swpp', sw_views.upload_swpp , name="service_del"),
    path('s/service/<int:service_id>', sw_views.view_service , name="service_edit"),
    path('s/date_by_service/<int:service_id>',date_views.date_by_service,name="date_by_service"),
    path('s/profile/', sw_views.my_profile, name="sw_my_profile"),
    path('s/dates/', sw_views.dates, name="sw_history"),
    path('s/payments/', ts_views.s_payments, name="sw_payments"),
    path('s/get_date_list_more_dates/<int:index>',sw_views.get_date_list_more_dates,name="s_get_date_list"),
    path('s/mc_panel/', sw_views.mc_panel, name="s_mc_panel"),
    path('s/update_mc/', sw_views.update_mc, name="update_mc"),
    #path('about/', da_views.about, name="about"),

    path('c/profile/s/<int:sw_id>',sw_views.public_profile,name="sw_public_profile"),
    path('c/date_form/<int:service_id>', date_views.date_form, name="form" ),

#   Client functionalities
    path('c/home/', client_views.home_c , name="home_c"),
    path('c/dates/', client_views.dates , name="dates"),
    path('c/profile/',client_views.my_profile,name="client_public_profile"),
    path('c/edit_profile/',client_views.edit_profile,name="client_public_profile"),
    path('c/get_service_list/<int:index>',client_views.get_service_list,name="c_get_service_list"),
    path('c/get_date_list/<int:index>',client_views.get_date_list,name="c_get_date_list"),
    path('c/payments/', ts_views.c_payments, name="sw_payments"),
    path('c/mc_panel/', client_views.mc_panel, name="c_mc_panel"),
    path('c/upload_cpp', client_views.upload_cpp , name="upload_client_profile_picture"),
    path('c/account_del/<int:client_id>', client_views.account_del , name="account_del"),
    path('c/update_mc/', client_views.update_mc, name="update_mc"),

#   QR
    path('generate_date/<int:service_id>', date_views.generate_date, name="generate_date"),
    path('createqr/<int:date_id>',date_views.createQR),
    path('qrcheck/<int:date_id>/<str:code>',date_views.checkQR),

#    Date states
    path('accept_date/<int:date_id>',date_views.accept_date,name='accept_date'),
    path('reject_date/<int:date_id>',date_views.reject_date,name='reject_date'),
    path('end_date/<int:date_id>',date_views.end_date,name='end_date'),
    path('pay_date/<int:date_id>',date_views.pay_date,name='pay_date'),
    path('pay_date_submit/<int:date_id>',date_views.pay_date_submit,name='pay_date_submit'),
    path('rate_date/<int:date_id>/<int:rate>',date_views.rate_date,name='rate_date'),

#   Payments
    path('c/charge/<int:date_id>', ts_views.charge, name='charge'),

    # Ajax
    path('ajax/user_exists', session_views.user_exists, name='user_exists'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'app_sessions.views.error_404_view'
