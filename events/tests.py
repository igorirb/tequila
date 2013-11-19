import datetime

from django.utils					import timezone
from django.test 					import TestCase

from events.models					import Event

class EventMethodTests(TestCase):

	def test_has_passed_with_future_event(self):
		"""
		should return false for events in the future
		"""
		time = timezone.now() + datetime.timedelta(days=10)
		future_event = Event(starts_at=time)
		self.assertEqual(future_event.has_passed(), False)

	def test_has_passed_with_past_event(self):
		"""
		should return false for events in the past
		"""
		time = timezone.now() - datetime.timedelta(days=10)
		future_event = Event(starts_at=time)
		self.assertEqual(future_event.has_passed(), True)