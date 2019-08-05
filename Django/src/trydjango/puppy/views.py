from django.shortcuts import render


# Create your views here.
def puppy_home_view(request):
    context = {}

    return render(request, 'puppy-home.html', context)
