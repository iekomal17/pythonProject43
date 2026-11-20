from django.shortcuts import render
from shop.models import Owner


def index(request):
    return render(request, 'manager/dashboard.html')


def main(request):
    registration = Owner.objects.all()
    return render(request, 'manager/show.html', {'registration': registration})

# Create your views here.
