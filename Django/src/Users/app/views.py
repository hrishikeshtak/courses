from django.shortcuts import render
from .models import User


# Create your views here.
def index_view(request):
    context = {}

    return render(request, "index.html", context)


def user_view(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {"users": user_list}

    return render(request, "users.html", context=user_dict)
