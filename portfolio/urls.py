from django.conf.urls import patterns, include, url
from portfolio import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^resume/$', views.resume, name='resume'),
)
