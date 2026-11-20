from django.contrib import admin
from .models import Owner


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('shopname', 'ownername', 'shopcategory', 'shopregno', 'license')

# Register your models here.
