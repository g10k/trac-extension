"""djtrac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin, auth
from django.contrib.auth.views import login, logout
from djtrac import views
from djtrac.forms import CustomAuthenticationForm

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login, {'template_name': 'djtrac/login.html','authentication_form': CustomAuthenticationForm}, name='custom_login'),
    url(r'^logout/$', logout, {'next_page': '/'}),
    url(r'^ac/keywords/', views.keywords),
    url(r'^$', views.main),
    url(r'^tickets/(?P<pk>[0-9]+)/$', views.TicketDetail.as_view(), name='ticket'),
]
