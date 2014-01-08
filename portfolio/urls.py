from django.conf.urls import patterns, include, url
from portfolio import views

urlpatterns = patterns('',
    url(r'^$', views.portfolio, name='portfolio'),
    url(r'^project/(?P<slug>[\w-]+)/$', views.project, name="project"),
    url(r'^resume/$', views.resume, name='resume'),
)
