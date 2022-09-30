from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
from django.core.management import call_command


def page_view(request):
    # call_command('scrape_all_job')
    context='done'

    return render(request, 'homepage.html')
