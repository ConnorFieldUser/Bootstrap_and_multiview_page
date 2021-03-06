"""Bootstraps_bootstraps URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from fan_app.views import index_view, joels_info_view, my_info_view, about_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view),
    url(r"^joels_info/", joels_info_view, name="joels_info_view"),
    url(r"^my_info/", my_info_view, name="my_info_view"),
    url(r"^about/", about_view, name="about_view")
]
