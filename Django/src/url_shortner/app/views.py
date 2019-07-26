from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from django.shortcuts import render

from .models import URLShortner
from .forms import URLShortnerForm

# URL Shortner using Base 62 method

# Domain name for Short URL ex. bitly.com
DOMAIN = "https://us.com"
# constant number that will be input to the Base62 encoding
CONSTANT = 100000000000  # to make short URL of length 7
ALPHABETS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
BASE = len(ALPHABETS)


class HomeView(TemplateView):

    def __init__(self):
        self.long_url = None

    def get(self, request):
        form = URLShortnerForm()
        return render(request, 'home.html', {'form': form})

    def post(self, request):
        form = URLShortnerForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            self.long_url = url
            # print('long_url: ', self.long_url)
            short_url = self.shortenUrl()
            # initialize empty form
            form = URLShortnerForm()

        args = {'form': form, 'short_url': short_url,
                'long_url': self.long_url}
        return render(request, 'home.html', args)

    def shortenUrl(self):
        """
        Encode a positive number in Base 62
        Input: Long URL
        Output: Short URL
        """
        global CONSTANT
        short_url = ""

        # convert constant number to Base-62 encoding
        CONSTANT += 1
        number = CONSTANT
        while number:
            short_url = ALPHABETS[number % BASE] + short_url
            number = number // BASE

        short_url = ("%s/%s") % (DOMAIN, short_url)

        # save data into database
        url_models = URLShortner(short_url=short_url,
                                 long_url=self.long_url,
                                 hits=1)
        url_models.save()
        return short_url


class GetURLDetails(TemplateView):

    def get(self, request):
        form = URLShortnerForm()
        return render(request, 'long_url.html', {'form': form})

    def post(self, request):
        """
        return long URL
        Input: Short URL
        Output: Long URL
        """
        form = URLShortnerForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            self.short_url = url
            print('short_url: ', self.short_url)
            result = self.expand_url()
            # initialize empty form
            form = URLShortnerForm()

        args = {'form': form, 'result': result}
        return render(request, 'long_url.html', args)

    def expand_url(self):
        # get URLs from database
        # check short url present in database
        result = {}
        # if present return actual URL
        url = URLShortner.objects.get(short_url=self.short_url)
        url.hits += 1
        result['long_url'] = url.long_url
        result['short_url'] = url.short_url
        result['total_hits'] = url.hits
        # increase hit count and update database
        url.save()
        if not result:
            return {}
        return result


@api_view(['GET'])
def getURLs_view(request, *args, **kwargs):
    """
    return all short => long URLs
    """
    # get URLs from database
    result = []
    if request.method == 'GET':
        urls = URLShortner.objects.all()
        for url in urls:
            data = {}
            data['long_url'] = url.long_url
            data['short_url'] = url.short_url
            data['total_hits'] = url.hits
            result.append(data)

    return render(request, 'urls.html', {'result': result})
    # return Response(result)
