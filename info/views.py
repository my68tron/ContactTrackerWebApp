from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
# from .models import EndUserProfile
from .forms import SearchForm, AdminLoginForm
from sync.models import Contact
from django.contrib.auth.decorators import login_required

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



@login_required
def track_user(request):
	search_form = SearchForm()
	contact_list = None
	if request.method == 'POST':
		search_form = SearchForm(data=request.POST)
		if search_form.is_valid():
			cd = search_form.cleaned_data
		contact_list1 = Contact.objects.filter(from_mob_no=cd['search_text']).order_by('timestamp')
		contact_list2 = Contact.objects.filter(to_mob_no=cd['search_text']).order_by('timestamp')
	return render(request, 'info/track.html', {'search_form':search_form, 'contact_list1': contact_list1,'contact_list2': contact_list2})





# def end_user_register(request):
# 	# if form filled
# 	if request.method == 'POST':
# 		form = EndUserRegistrationForm(data=request.POST)

# 		if form.is_valid():
# 			new_profile = form.save()

# 			return HttpResponse("Success register!")
# 	# if new form to be rendered
# 	else:
# 		form = EndUserRegistrationForm()


# 	return render(request, 'info/register.html', context={'form':form,})
