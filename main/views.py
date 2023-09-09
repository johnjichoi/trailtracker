from django.contrib import messages
from django.contrib.auth import (
    authenticate,
	login, 
    logout
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import (
    redirect,
	render
)

from .forms import NewUserForm

def homepage_request(request):
	if request.user.is_authenticated:
		return redirect('main:trails')
		
	return render(request=request, template_name='homepage.html')

@login_required
def trails_request(request):
	return render(request=request, template_name='trails.html')

def register_request(request):
	if request.method != 'POST':
		return render(
			request = request,
			template_name = 'register.html',
			context = {'register_form': NewUserForm()}
		)
	
	form = NewUserForm(request.POST)

	if not form.is_valid():
		messages.error(request, 'Registration failed')
		return render(request=request, template_name='register.html', context={'register_form':form})

	user = form.save()
	login(request, user)
	messages.success(request, 'Registration succeeded')
	return redirect('main:homepage')

def login_request(request):
	if request.method != 'POST':
		return render(
			request = request,
			template_name = 'login.html',
			context = {'login_form': AuthenticationForm()}
		)
	
	form = AuthenticationForm(request, data=request.POST)
	if not form.is_valid():
		messages.error(request,'Invalid username or password.')
		return render(request=request, template_name='login.html', context={'login_form':form})
	
	username = form.cleaned_data.get('username')
	password = form.cleaned_data.get('password')
	user = authenticate(username=username, password=password)
		
	if user is None:
		messages.error(request,'Invalid username or password.')
		return render(request=request, template_name='login.html', context={'login_form':form})
	
	login(request, user)
	return redirect('main:homepage')
	
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("main:homepage")
	