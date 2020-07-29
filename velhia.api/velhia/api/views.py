from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Regions, Languages, Currencies, Games, Symbols, Positions
from .models import Countries, Players, Matchs, Moves
from .serializers import RegionSerializer, LanguageSerializer, CurrencySerializer, GameSerializer, SymbolSerializer, PositionSerializer 
from .serializers import CountrySerializer, PlayerSerializer, MatchSerializer, MoveSerializer


class RegionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Regions.objects.all()
    serializer_class = RegionSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Languages.objects.all()
    serializer_class = LanguageSerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Currencies.objects.all()
    serializer_class = CurrencySerializer


class GameViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Games.objects.all()
    serializer_class = GameSerializer


class SymbolViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Symbols.objects.all()
    serializer_class = SymbolSerializer


class PositionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Positions.objects.all()
    serializer_class = PositionSerializer


class CountryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Countries.objects.all()
    serializer_class = CountrySerializer

    def create(self, request):
        data = request.data
        new_country = Countries.objects.create(
            Name = data['Name'],
            Country_code = data['Country_code'],
            Region = Regions.objects.get(Id=data['Region']),
            Language = Languages.objects.get(Id=data['Language']),
            Currency = Currencies.objects.get(Id=data['Currency'])

        )

        new_country.save()
        serializer = CountrySerializer(new_country)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        data = request.data
        old_country = Countries.objects.get(Id=pk)
        old_country.Name = data['Name']
        old_country.Country_code = data['Country_code']
        old_country.Region = Regions.objects.get(Id=data['Region'])
        old_country.Language = Languages.objects.get(Id=data['Language'])
        old_country.Currency = Currencies.objects.get(Id=data['Currency'])

        old_country.save()
        serializer = CountrySerializer(old_country)
        return Response(serializer.data)


class PlayerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Players.objects.all()
    serializer_class = PlayerSerializer

    def create(self, request):
        data = request.data
        new_player = Players.objects.create(
            Name = data['Name'],
            Lastname = data['Lastname'],
            Email = data['Email'],
            Country = Countries.objects.get(Id=data['Country']),
            Genre = data['Genre'],
            Age = data['Age']

        )
        
        new_player.save()
        serializer = PlayerSerializer(new_player)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        data = request.data
        old_player = Players.objects.get(Id=pk)
        old_player.Name = data['Name']
        old_player.Lastname = data['Lastname']
        old_player.Email = data['Email']
        old_player.Country = Countries.objects.get(Id=data['Country'])
        old_player.Genre = data['Genre']
        old_player.Age = data['Age']

        old_player.save()
        serializer = PlayerSerializer(old_player)
        return Response(serializer.data)


class MoveViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Moves.objects.all()
    serializer_class = MoveSerializer

    def create(self, request):
        data = request.data
        new_moves = Moves.objects.create(
            Player = Players.objects.get(Id=data['Player']),
            Position = Positions.objects.get(Id=data['Position']),
            Symbol = Symbols.objects.get(Id=data['Symbol'])
        )
        
        new_moves.save()
        serializer = MoveSerializer(new_moves)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        data = request.data
        old_move = Players.objects.get(Id=pk)
        old_move.Player = Players.objects.get(Id=data['Player'])
        old_move.Position = Positions.objects.get(Id=data['Position'])
        old_move.Symbol = Symbols.objects.get(Id=data['Symbol'])

        old_move.save()
        serializer = MoveSerializer(old_move)
        return Response(serializer.data)


class MatchViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Matchs.objects.all()
    serializer_class = MatchSerializer

    def create(self, request):
        data = request.data

        new_match = Matchs.objects.create(
            Game = Games.objects.get(Id=data['Game'])
        )

        plays = self.fillObjects(Players, data['Plays'])
        moves = self.fillObjects(Moves, data['Moves'])

        new_match.save()
        new_match.Plays.set(plays)
        new_match.Moves.set(moves)

        serializer = MoveSerializer(new_match)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        data = request.data
        plays = self.fillObjects(Players, data['Plays'])
        moves = self.fillObjects(Moves, data['Moves'])

        old_match = Matchs.objects.get(Id=pk)
        old_match.Game = Games.objects.get(Id=data['Game'])
        old_match.Plays.set(plays)
        old_match.Moves.set(moves)

        old_match.save()
        serializer = MatchSerializer(old_match)
        return Response(serializer.data)

    def fillObjects(self, obj, array):
        result = []
        for i in array:
            result.append(obj.objects.get(Id=i))
        return result
