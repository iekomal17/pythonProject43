from django.core import validators
from django import forms
from .models import Owner


class ShopRegistration(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['shopname', 'ownername', 'shopcategory', 'shopregno', 'license']
        labels = {'shopename': 'Enter Shop Name', 'ownername': 'Enter Name', 'shopcategory': 'Enter category', 'shopregno': 'Enter Registration No', 'license': 'License Available'}
