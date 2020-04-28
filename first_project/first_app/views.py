from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

def index(request):
    my_dict = {'insert_me': 'Hello im from views.py'}
    return render(request, 'first_app/index.html', context=my_dict)

def dataPage(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'first_app/data.html', date_dict)
