from django.shortcuts import render
from .form import ShopRegistration
from django.http import HttpResponse
from django.template import loader
from .models import Owner
from mall import settings
from django.core.mail import send_mail


def first(request):
    template = loader.get_template('welcome.html')
    return HttpResponse(template.render())


def second(request):
    if request.method == 'POST':
        fm = ShopRegistration(request.POST)
        if fm.is_valid():
            sn = fm.cleaned_data['shopname']
            on = fm.cleaned_data['ownername']
            sc = fm.cleaned_data['shopcategory']
            srn = fm.cleaned_data['shopregno']
            lse = fm.cleaned_data['license']
            fm = ShopRegistration()
            print(sn)
            print(on)
            print(sc)
            print(srn)
            reg = Owner(shopname=sn, ownername=on, shopcategory=sc, shopregno=srn, license=lse)
            reg.save()
    else:
        fm = ShopRegistration()
    return render(request, 'shopreg.html', {'form': fm})


def third(request):
    template = loader.get_template('gallary.html')
    return HttpResponse(template.render())


def fourth(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())


# Create your views here.
def mail(request):
    subject = "complaint"
    msg = "complaint raise by someone"
    to = "komalingale732@gmail.com"
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if res == 1:
        msg = "mail sent successfuly"
    else:
        msg = "mail could not send"
    return HttpResponse(msg)
