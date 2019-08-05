# from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    print("request: %s args: %s, kwargs: %s" % (
        request, args, kwargs))
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, 'home.html', {})


def about_view(request, *args, **kwargs):
    print("request: %s args: %s, kwargs: %s" % (
        request, args, kwargs))
    # return HttpResponse("<h1>About view</h1>")
    my_context = {
        "my_text": "This is about me",
        "my_list": [1, 2, 3, 4]
    }
    return render(request, 'about.html', my_context)
