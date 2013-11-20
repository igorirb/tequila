import datetime

from django.db 						import models
from django.forms 					import ModelForm
from django.utils 					import timezone
from django.contrib.auth.models 	import User
from app.models 					import Performer, Contact

class Place(models.Model):
	name 					= models.CharField(max_length=64, blank=True)
	street					= models.CharField(max_length=64, blank=True)
	number 					= models.CharField(max_length=16, blank=True)
	neighborhood			= models.CharField(max_length=64, blank=True)
	zipcode					= models.CharField(max_length=16, blank=True)
	city					= models.CharField(max_length=128, blank=True)
	state					= models.CharField(max_length=4, blank=True)
	country					= models.CharField(max_length=64, blank=True)
	latitude				= models.CharField(max_length=16, blank=True)
	longitude 				= models.CharField(max_length=16, blank=True)

class Event(models.Model):
	title					= models.CharField(max_length=64, blank=False)
	facebook_page			= models.CharField(max_length=256, blank=True)
	starts_at				= models.DateTimeField(blank=False)
	ends_at					= models.DateTimeField(blank=True)
	description				= models.TextField(blank=False)
	contacts				= models.ManyToManyField(Contact, through='EventContact')
	performers				= models.ManyToManyField(Performer, through='EventPerformer')
	place 					= models.ForeignKey(Place, blank=False)
	admin					= models.ForeignKey(User, blank=False)

	def has_passed(self):
		return self.starts_at <= timezone.now() - datetime.timedelta(days=1)
	has_passed.admin_order_field = 'starts_at'
	has_passed.boolean = True
	has_passed.short_description = 'Event has passed?'

class EventPerformer(models.Model):
	event 					= models.ForeignKey(Event)
	performers 				= models.ForeignKey(Performer)

class EventContact(models.Model):
	event 					= models.ForeignKey(Event)
	contact 				= models.ForeignKey(Contact)

class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ('starts_at', 'ends_at')
		labels = {
            'starts_at': ('Inicio'),
            'ends_at': ('Fim'),
        }