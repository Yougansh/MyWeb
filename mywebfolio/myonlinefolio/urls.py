from django.conf.urls import patterns, url

from myonlinefolio import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),


    )
