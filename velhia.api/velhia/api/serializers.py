from rest_framework import serializers
from .models import Regions, Languages, Currencies, Games, Symbols, Positions
from .models import Countries, Players, Matchs, Moves


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Regions
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Languages
        fields = '__all__'


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currencies
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = '__all__'


class SymbolSerializer(serializers.ModelSerializer):

    class Meta:
        model = Symbols
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Positions
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Countries
        fields = '__all__'
        depth = 1


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Players
        fields = '__all__'
        depth = 2


class MatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Matchs
        fields = '__all__'
        depth = 3


class MoveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Moves
        fields = '__all__'
        depth = 3
