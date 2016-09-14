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
    url(r'^load_loan_number/$', views.load_submit)
]
