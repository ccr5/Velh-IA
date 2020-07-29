from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegionViewSet, LanguageViewSet, CurrencyViewSet, GameViewSet, SymbolViewSet, PositionViewSet
from .views import CountryViewSet, PlayerViewSet, MoveViewSet, MatchViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'regions', RegionViewSet, basename='region')
router.register(r'languages', LanguageViewSet, basename='language')
router.register(r'currencies', CurrencyViewSet, basename='currency')
router.register(r'games', GameViewSet, basename='game')
router.register(r'symbols', SymbolViewSet, basename='symbol')
router.register(r'positions', PositionViewSet, basename='position')
router.register(r'countries', CountryViewSet, basename='country')
router.register(r'players', PlayerViewSet, basename='player')
router.register(r'moves', MoveViewSet, basename='move')
router.register(r'matchs', MatchViewSet, basename='match')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]