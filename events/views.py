import urllib
from datetime 						import datetime
from django.http 					import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts 				import render, get_object_or_404, get_list_or_404
from events.models 					import Event

def event(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	return render(request, 'events/event.html', { 'event': event })

def events(request, starts_at, ends_at):
	events = list(Event.objects.filter(starts_at__gte=datetime(int(starts_at[0:4]), int(starts_at[4:6]), int(starts_at[6:8]))))
	if not events: 
		raise Http404
	for e in events:
		e.url = urllib.quote_plus(e.title + ' ' + e.starts_at.strftime('%Y %m %d')).lower().replace('+', '-')
	return render(request, 'events/index.html', { 'events': events })