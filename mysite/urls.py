"""mysite URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from base import views as base_views
# from base import post as post_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', base_views.index),
    # url(r'^index/$', base_views.index),
    # url(r'^info/$', base_views.info),
    # url(r'^login/$', base_views.login),
    # url(r'^test/$', post_views.list),
    url(r'^base/', include('base.urls')),
]
