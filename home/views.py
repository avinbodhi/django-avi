from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import serializers
from home.models import Visit
from rest_framework.renderers import JSONRenderer
from rest_framework import serializers
from .serializers import VisitSerializer
import requests

# Create your views here.


def index(request):
    # return HttpResponse("Hello!! I am on homepage")
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        noofguest = request.POST.get('noofguest')
        typeofacc = request.POST.get('typeofacc')
        # return HttpResponse(fromdate)
        Visit111 = Visit(fromdate=fromdate, todate=todate,
                         noofguest=noofguest, typeofacc=typeofacc)
        Visit111.save()

    data = {
        "title": "Home Page",
        "description": "BAAP AGRO!!!"
    }
    return render(request, 'index.html', data)


def contact(request):
    # return HttpResponse("Hello!! I am on contact~!")
    return render(request, 'contact.html')


def visit_details(request, pk):
    # collect the data
    visit_details = Visit.objects.get(id=pk)
    # converting data with serializer
    serializer_data = VisitSerializer(visit_details)
    # print(serializer_data)

    # serializer to json
    json_data = JSONRenderer().render(serializer_data.data)
    return HttpResponse(json_data)


def visit_list(request):
    visit_details = Visit.objects.all()
    # converting data with serializer
    serializer_data = VisitSerializer(visit_details, many=True)
    # serializer to json
    json_data = JSONRenderer().render(serializer_data.data)
    return HttpResponse(json_data)
    # print(serializer_data)

# get the data from API request and use this data in HTML file / view file


def VisitHomePage(request):
    url = 'http://localhost:8000/visitall'
    r = requests.get(url=url)
    data = r.json()
    return render(request, 'index.html', {'response': data})
