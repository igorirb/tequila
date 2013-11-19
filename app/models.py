from django.db 						import models
from django.utils 					import timezone
from django.contrib.auth.models 	import User

class Profile(models.Model):
	user 					= models.OneToOneField(User)
	picture					= models.CharField(max_length=128, blank=True)
	gender_choices 			= (('M', 'Masculino'), ('F', 'Feminino'))
	gender 					= models.CharField(max_length=1, choices=gender_choices, blank=True)
	date_of_birth 			= models.DateField(null=True, blank=True)
	city 					= models.CharField(max_length=64, blank=True)
	state					= models.CharField(max_length=4, blank=True)
	phone_number 			= models.CharField(max_length=16, blank=True)
	date_joined 			= models.DateTimeField(default=timezone.now)

class Contact(models.Model):
	first_name 				= models.CharField(max_length=32, blank=True)
	last_name 				= models.CharField(max_length=32, blank=True)
	email 					= models.EmailField(max_length=128, blank=True)
	phone_number 			= models.CharField(max_length=16, blank=True)
	website					= models.CharField(max_length=128, blank=True)

class Performer(models.Model):
	name 					= models.CharField(max_length=64, blank=True)
	facebook_page			= models.CharField(max_length=256, blank=True)
	# GENRE LIST
	AXE						= 'AXE'
	BOSSANOVA				= 'BSN'
	CLASSICAL				= 'CLS'
	ELECTRONIC				= 'ELE'
	FORRO					= 'FOR'
	FUNK					= 'FNK'
	PAGODE					= 'PGD'
	POP						= 'POP'
	RAP						= 'RAP'
	ROCK 					= 'RCK'
	SAMBA					= 'SMB'
	SERTANEJO				= 'STJ'
	UNKNOWN 				= 'UNK'
	MUSIC_GENRE_CHOICES = (
        (AXE, 'Axe'),
        (BOSSANOVA, 'Bossa Nova'),
        (CLASSICAL, 'Classical'),
        (ELECTRONIC, 'Electronic'),
        (FORRO, 'Forro'),
        (FUNK, 'Funk'),
        (PAGODE, 'Pagode'),
        (POP, 'Pop'),
        (RAP, 'Rap'),
        (ROCK, 'Rock'),
        (SAMBA, 'Samba'),
        (SERTANEJO, 'Sertanejo'),
        (UNKNOWN, 'Unknown'),
	)
	genre = models.CharField(max_length=3, choices=MUSIC_GENRE_CHOICES, default=UNKNOWN)

