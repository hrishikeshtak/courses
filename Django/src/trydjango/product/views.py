from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Product

from .forms import RawProductForm, ProductForm


def dynamic_lookup_view(request, my_id):
    # obj = get_object_or_404(Product, id=my_id)
    try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        'object': obj
    }

    return render(request, 'product/product_dynamic.html', context)


def all_product_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }

    return render(request, 'product/product_details.html', context)


# Create your views here.
def product_details_view(request):
    initial_data = {
        'title': "Product Title"
    }
    my_form = ProductForm(request.POST or None, initial=initial_data)
    if my_form.is_valid():
        my_form.save()
        my_form = ProductForm()

    context = {
        "form": my_form
    }

    return render(request, 'product/product_details.html', context)


def create_detail_view(request):
    my_form = RawProductForm()  # GET method to show initial layout of form
    if request.method == 'POST':
        my_form = RawProductForm(request.POST)
        # my_title = request.POST.get('title')
        # print("my_title: ", my_title)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        'form': my_form
    }

    return render(request, 'product/create_detail.html', context)
