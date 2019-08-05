from django.urls import path
from .views import puppy_home_view


urlpatterns = [
    path('', puppy_home_view, name='home'),
]
