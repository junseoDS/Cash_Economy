
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    path('admin/', admin.site.urls),
    path('sign/', include('sign.urls')),


]
