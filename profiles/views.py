from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import EndUserProfile
from .forms import EndUserRegistrationForm, AdminLoginForm


def end_user_register(request):
	# if form filled
	if request.method == 'POST':
		form = EndUserRegistrationForm(data=request.POST)

		if form.is_valid():
			new_profile = form.save()

			return HttpResponse("Success register!")
	# if new form to be rendered
	else:
		form = EndUserRegistrationForm()


	return render(request, 'profiles/register.html', context={'form':form,})


