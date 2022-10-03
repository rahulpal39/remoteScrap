from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
from django.core.management import call_command


def page_view(request):

    if request.method == 'POST':
        data=request.POST['search']
        # c = RequestContext(request.POST, {
        response=call_command('scrape_all_job')

        print(response)


    return render(request, 'homepage.html')
