"""djtrac URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from djtrac.forms import CustomAuthenticationForm
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login, {'template_name': 'djtrac/login.html','authentication_form': CustomAuthenticationForm}, name='custom_login'),
    url(r'^logout/$', logout, {'next_page': '/'}),
    url(r'^$', 'djtrac.views.main.main'),
    url(r'^(\d+)/release_note/$', 'djtrac.views.release_note.edit'),
    url(r'^send_release_note/$', 'djtrac.views.release_note.send_mail'),
    url(r'^select2/', include('django_select2.urls')),
]

urlpatterns += static('npm', document_root=settings.BASE_DIR + '/node_modules', show_indexes=True)
