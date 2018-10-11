from django.contrib import admin
from .models import *


@admin.register(Ticket)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'check_in')
