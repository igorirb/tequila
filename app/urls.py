from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^profile/(?P<user_id>\d+)/$', views.profile, name='profile'),
)