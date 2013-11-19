from django.shortcuts 				import render, get_object_or_404
from app.models 					import Profile

def index(request):
    return render(request, 'app/index.html')

def profile(request, user_id):
	profile = get_object_or_404(Profile, user_id=user_id)
	return render(request, 'app/profile.html', { 'profile': profile })
