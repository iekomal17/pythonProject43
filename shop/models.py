from django.db import models


class Owner(models.Model):
    shopname = models.CharField(max_length=255)
    ownername = models.CharField(max_length=255)
    shopcategory = models.CharField(max_length=255)
    shopregno = models.CharField(max_length=255)
    license = models.CharField(max_length=255)

