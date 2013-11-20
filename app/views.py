from django.shortcuts 				import render, get_object_or_404, render_to_response
from django.template				import RequestContext
from app.models 					import Profile, UserForm
from events.models 					import EventForm
from django.contrib.auth 			import authenticate, logout, login
from django.http 					import HttpResponseRedirect, HttpResponse

def index(request):
	user = request.user
	if user is not None:
		form = UserForm()
		return render(request, 'app/index.html', {
	    	'form': form,
	    })
	else:
		form = EventForm()
		return render(request, 'app/search.html', {
	    	'form': form,
	    })

def search_view(request):
	form = EventForm()
	return render(request, 'app/search.html', {
    	'form': form,
    })

def login_view(request):
	email = password = ''
	if request.POST:
		username = 'igor'
		password = 'caio1992'

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/search')

	form = UserForm()
	return render_to_response('app/index.html', {'form': form}, context_instance=RequestContext(request))

def logout_view(request):
	logout(request)

def profile(request, user_id):
	profile = get_object_or_404(Profile, user_id=user_id)
	return render(request, 'app/profile.html', { 'profile': profile })
