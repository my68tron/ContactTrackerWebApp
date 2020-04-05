from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
import os

# Index page of sync with details and rules to setup sync
def index(request):
    return HttpResponse("Hello. You're at the sync index.")

# Initialise Android and register user by taking in his details
@csrf_exempt
def initialise(request):
    if request.method == 'POST':
        request_body = json.loads(request.body.decode('utf-8'))
        if 'mob_no' in request_body:
            return HttpResponse('OK')
    return HttpResponseBadRequest("Bad Request")

# Update Android data
@csrf_exempt
def update(request):
    if request.method == 'POST':
        request_body = json.loads(request.POST['jsonData'])
        if request.FILES.getlist('uploadedFile') != None:
            return HttpResponse('OK')
    return HttpResponseBadRequest("Bad Request")