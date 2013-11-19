from django.contrib 				import admin
from django.utils 					import timezone
from events.models 					import Event, Place

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
    	(None, {'fields': ['title', 'description', 'facebook_page']}),
    	('Date information', {'fields': ['starts_at', 'ends_at']}),
    	('Place information', {'fields': ['place']}),
    	('Admin information', {'fields': ['admin']}),
    ]
    list_display = ('title', 'starts_at', 'ends_at', 'has_passed')

admin.site.register(Event, EventAdmin)
admin.site.register(Place)
