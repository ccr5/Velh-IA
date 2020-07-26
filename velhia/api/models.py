from django.db import models
from django.contrib.postgres.fields import ArrayField, HStoreField


class Regions(models.Model):
    Id = models.AutoField(primary_key=True, verbose_name="region")
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = 'Regions'


class Languages(models.Model):
    Id = models.AutoField(primary_key=True, verbose_name="language")
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = 'Languages'


class Currencies(models.Model):
    Id = models.AutoField(primary_key=True, verbose_name="currency")
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = 'Currencies'


class Countries(models.Model):
    Id = models.AutoField(primary_key=True, verbose_name="country")
    Name = models.CharField(max_length=50)
    Country_code = models.CharField(unique=True, max_length=3)
    Region = models.ForeignKey(Regions, related_name='Region', on_delete=models.CASCADE)
    Language = models.ForeignKey(Languages, related_name='Language', on_delete=models.CASCADE)
    Currency = models.ForeignKey(Currencies, related_name='Currency', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = 'Countries'


class Players(models.Model):
    Id = models.AutoField(primary_key=True, null=False, blank=False, verbose_name="player")
    Name = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    Country = models.ForeignKey(Countries, related_name='Country', on_delete=models.CASCADE)
    Genre = models.CharField(max_length=50)
    Age = models.IntegerField()

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = 'Players'


class Games(models.Model):
    Id = models.AutoField(primary_key=True, verbose_name="game")
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = 'Games'


class Symbols(models.Model):
    Id = models.AutoField(primary_key=True, null=False, blank=False, verbose_name="symbol")
    Character = models.CharField(max_length=1)

    def __str__(self):
        return self.Character

    class Meta:
        verbose_name_plural = 'Symbols'


class Positions(models.Model):
    Id = models.IntegerField(primary_key=True, unique=True, verbose_name="position")
    Name = models.CharField(max_length=4)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = 'Positions'
        ordering = ['Id']


class Moves(models.Model):
    Id = models.AutoField(primary_key=True, verbose_name="Move")
    Player = models.ForeignKey(Players, related_name='Player', on_delete=models.CASCADE)
    Position = models.ForeignKey(Positions, related_name='Position', on_delete=models.CASCADE)
    Symbol = models.ForeignKey(Symbols, related_name='Symbol', on_delete=models.CASCADE)

    def __str__(self):
        return self.Player + '/' + self.Position + '/' + self.Symbol 

    class Meta:
        verbose_name_plural = 'Moves'
        ordering = ['Id']


class Matchs(models.Model):
    Id = models.AutoField(primary_key=True, verbose_name="Match")
    Game = models.ForeignKey(Games, related_name='Game', on_delete=models.CASCADE)
    Plays = models.ManyToManyField(Players)
    Moves = models.ManyToManyField(Moves)

    def __str__(self):
        return 'Match'

    class Meta:
        verbose_name_plural = 'Matchs'
        ordering = ['Id']
