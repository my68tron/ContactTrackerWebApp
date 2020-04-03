from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

# Index page of info app
def index(request):
    return render(request, 'info/index.html')

# About Page
def about(request):
    return render(request, 'info/about.html')

# Contact Page
def contact(request):
    return render(request, 'info/contact.html')
