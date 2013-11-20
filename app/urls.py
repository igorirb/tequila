from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^search$', views.search_view, name='search'),
	url(r'^login$', views.login_view, name='login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
	url(r'^profile/(?P<user_id>\d+)/$', views.profile, name='profile'),
)