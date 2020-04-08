from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from sync.models import Contact
import json
import csv
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
        filesList = request.FILES.getlist('contacts_info')
        fileName = handle_uploaded_file(filesList[0])
        from_mob_no = int(filesList[0].name)
        with open(fileName, 'r') as f:
            index = 0
            csvFile = csv.reader(f)
            for row in csvFile:
                contact = Contact.objects.create(from_mob_no=from_mob_no, to_mob_no=int(row[0]), timestamp=row[1])
                index += 1
        os.remove(fileName)
        print('Total Contacts :', index)
        return JsonResponse({'total_contacts': index})
    return HttpResponseBadRequest("Bad Request")