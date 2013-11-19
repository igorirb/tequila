from django.conf.urls import patterns, url

from events import views

urlpatterns = patterns('',
	url(r'^/(?P<event_id>\d+)/(.*/)?$', views.event, name='event'),
	url(r'^s/(?P<starts_at>\d+)/(?P<ends_at>\d+)/$', views.events, name='events'),
)