from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from profiles.forms import EndUserRegistrationForm, AdminLoginForm
# Index page of info app
def index(request):
	# logout required for login
	if request.user.is_authenticated:
		return HttpResponseRedirect("admin/")

	# if form filled
	if request.method == 'POST':
		login_form = AdminLoginForm(data=request.POST)

		if login_form.is_valid():
			cd = login_form.cleaned_data
			user = authenticate(request, username=cd['username'], password=cd['password'])


			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect("admin/")

				else:
					return HttpResponse("Account Terminated!")

			else:
				return HttpResponse("User Doesnt exist!")

	# if new form is to be rendered
	else:
		login_form = AdminLoginForm()


	return render(request, 'info/index.html', context={'login_form': login_form})
    

# About Page
def about(request):
    return render(request, 'info/about.html')

# Contact Page
def contact(request):
    return render(request, 'info/contact.html')
