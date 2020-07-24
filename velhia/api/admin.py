from django.contrib import admin
from .models import Regions, Countries, Currencies, Languages, Players, Games, Symbols, Positions, Matchs

admin.site.register(Regions)
admin.site.register(Languages)
admin.site.register(Currencies)
admin.site.register(Countries)
admin.site.register(Players)
admin.site.register(Games)
admin.site.register(Symbols)
admin.site.register(Positions)
admin.site.register(Matchs)
