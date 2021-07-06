from django.contrib import admin as dj_admin
from django_neomodel import admin as neo_admin

from .models import Entity
#  from .address import Address
#  from .intermediary import Intermediary
#  from .officer import Officer
#  from .other import Other

class EntityAdmin(dj_admin.ModelAdmin):
    list_display = ("name",)
neo_admin.register(Entity, EntityAdmin)

