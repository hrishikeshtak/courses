from django import forms


class URLShortnerForm(forms.Form):
    url = forms.URLField(label='URL', max_length=2048)
