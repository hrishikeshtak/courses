from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(
        attrs={
            "placeholder": "Your Title"
        }))
    email = forms.EmailField()
    description = forms.CharField(required=False)
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price"
        ]

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if 'CFE' not in title:
            raise forms.ValidationError("This is not a valid title")

        return title

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('edu'):
            raise forms.ValidationError("This is not a valid email")

        return email


class RawProductForm(forms.Form):
    title = forms.CharField(label='Title', widget=forms.TextInput(
        attrs={
            "placeholder": "Your Title"
        }))
    description = forms.CharField(required=False)
    price = forms.DecimalField(initial=199.99)
