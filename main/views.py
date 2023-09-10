from django.contrib import messages
from django.contrib.auth import (
    authenticate,
	login, 
    logout
)
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import (
    redirect,
	render
)

from .forms import NewUserForm

def main_request(request):
	if request.user.is_authenticated:
		return redirect('trip:trip')
		
	return render(request=request, template_name='main.html')

def register_request(request):
	if request.method != 'POST':
		form = NewUserForm()

		return render(
			request = request,
			template_name = 'register.html',
			context = {'register_form': form}
		)
	
	form = NewUserForm(request.POST)

	if not form.is_valid():
		messages.error(request, 'Registration failed')
		return render(request=request, template_name='register.html', context={'register_form':form})

	user = form.save()
	login(request, user)
	messages.success(request, 'Registration succeeded')
	return redirect('main:main')

def login_request(request):
	if request.method != 'POST':
		form = AuthenticationForm()
		return render(
			request = request,
			template_name = 'login.html',
			context = {'login_form': form}
		)
	
	form = AuthenticationForm(request, data=request.POST)
	if not form.is_valid():
		messages.error(request,'Login failed.')
		return render(request=request, template_name='login.html', context={'login_form':form})
	
	username = form.cleaned_data.get('username')
	password = form.cleaned_data.get('password')
	user = authenticate(username=username, password=password)
		
	if user is None:
		messages.error(request,'Login failed.')
		return render(request=request, template_name='login.html', context={'login_form':form})
	
	login(request, user)
	return redirect('trip:trip')
	
def logout_request(request):
	logout(request)
	messages.info(request, "Successfully logged out.") 
	return redirect("main:main")
	