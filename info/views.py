from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from info.forms import SearchForm, AdminLoginForm
from info.models import Contact
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
import csv
import os


# Index page of info app
def index(request):
    # logout required for login
    if request.user.is_authenticated:
        return HttpResponseRedirect("track/")

    # if form filled
    if request.method == 'POST':
        login_form = AdminLoginForm(data=request.POST)

        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("track/")

                else:
                    return HttpResponse("Account Terminated!")

            else:
                return HttpResponse("User Doesnt exist!")

    # if new form is to be rendered
    else:
        login_form = AdminLoginForm()
    return render(request, 'info/index.html', context={'login_form': login_form})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect('/')


# About Page
def about(request):
    return render(request, 'info/about.html')


# Contact Page
def contact(request):
    return render(request, 'info/contact.html')


@login_required
def track_user(request):
    search_form = SearchForm()
    contact_list1 = None
    contact_list2 = None
    if request.method == 'POST':
        search_form = SearchForm(data=request.POST)
        if search_form.is_valid():
            cd = search_form.cleaned_data
        contact_list1 = Contact.objects.filter(
            from_mob_no=cd['search_text']).order_by('timestamp')
        contact_list2 = Contact.objects.filter(
            to_mob_no=cd['search_text']).order_by('timestamp')
    return render(request, 'info/track.html', {'search_form': search_form, 'contact_list1': contact_list1, 'contact_list2': contact_list2})


def handle_uploaded_file(f):
    name = os.path.join(settings.MEDIA_DIR, f.name + ".csv")
    with open(name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return name


# Update Contact data
@csrf_exempt
def update(request):
    if request.method == 'POST':
        request_body = json.loads(request.body.decode('utf-8'))
        from_mob_no = request_body['from_mob_no']

        for row in request_body['contacts']:
            try:
                contact = Contact.objects.get(
                    from_mob_no=from_mob_no, to_mob_no=row['to_mob_no'])
            except Contact.DoesNotExist:
                try:
                    contact = Contact.objects.get(
                        from_mob_no=row['to_mob_no'], to_mob_no=from_mob_no)
                except Contact.DoesNotExist:
                    contact = Contact(from_mob_no=from_mob_no,
                                      to_mob_no=row['to_mob_no'])
            contact.timestamp = row['timestamp']
            contact.save()

        return JsonResponse({
            'result': True,
            'total_contacts': len(request_body['contacts'])
        })
    return HttpResponseBadRequest("Bad Request")
