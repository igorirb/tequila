from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('app.urls', namespace='app')),
    url(r'^event', include('events.urls', namespace='events')),
    url(r'^admin/', include(admin.site.urls)),
)
