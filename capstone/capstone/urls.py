"""capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls  vimport url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from submittals import views
from rest_framework import routers
from submittals.api import SubmittalViewSet

router = routers.DefaultRouter()
router.register(r'submits', SubmittalViewSet)

urlpatterns = [
    # Django Admin Site
    url(r'^admin/', admin.site.urls),

    # Web Application
    url(r'^$', views.index),

    # Accounts
    url(r'^login_user/$', views.login_user),
    url(r'^logout_user/$', views.logout_user),

    # Submittals
    url(r'^(?P<username>\w+)/submittals/new/$', views.submittals, name='submittals'),
    url(r'^save/', views.save_submit),
    url(r'^(?P<username>\w+)/submittals/$', views.dashboard, name='dashboard'),
    url(r'^(?P<username>\w+)/submittals/(?P<pk>\d+)/$', views.load_submit, name='load_submit'),
    url(r'^load_loan_number/$', views.load_submit),
    url(r'^delete/$', views.delete_submit, name='delete_submit'),
    url(r'^sms/$', views.sms_message, name='sms_message'),
    url(r'^get-zestimate/$', views.get_zestimate, name="get_zestimate"),

    #REST API
    url(r'api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^calculate/$', views.calculate_income, name='calculate_income'),

]
