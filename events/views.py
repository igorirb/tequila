import urllib

from django.shortcuts import render, get_object_or_404, get_list_or_404

from events.models import Event

def event(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	return render(request, 'events/event.html', { 'event': event })

def events(request, starts_at, ends_at):
	events = get_list_or_404(Event.objects.order_by('-starts_at'))
	for e in events:
		e.url = urllib.quote_plus(e.title + ' ' + e.starts_at.strftime('%Y %m %d')).lower().replace('+', '-')
	return render(request, 'events/index.html', { 'events': events })