from django.contrib import admin
from .models import Region, Country, Currency, Language, Player

admin.site.register(Region)
admin.site.register(Language)
admin.site.register(Currency)
admin.site.register(Country)
admin.site.register(Player)
