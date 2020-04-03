from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

# Index page of info app
def index(request):
    return HttpResponse("Hello. You're at the info app index.")

# About Page
def about(request):
    return HttpResponse("Hello. You're at the about page.")

# Contact Page
def contact(request):
    return HttpResponse("Hello. You're at the contact page.")
