from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    context = {}
    print(dir(request))
    return render(request, 'home.html', context)


def setsession(request):
    request.session['name'] = "hrishikesh"
    request.session['email'] = "abc@gmail.com"

    response = HttpResponse("Cookie Set")
    response.set_cookie('java-tutorial', 'javatpoint.com')


    return response


def getsession(request):
    name = request.session['name']
    email = request.session['email']

    print(request.session)

    return HttpResponse("Hi: %s, Email: %s" % (name, email))
