from django.http.response import HttpResponse
from django.shortcuts import render
from home.models import Visit
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
