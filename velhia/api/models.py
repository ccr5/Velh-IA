from django.db import models
from django.contrib.postgres.fields import ArrayField, HStoreField


class Regions(models.Model):
    Id = models.AutoField(primary_key=True, verbose_name="region")
    Name = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = 'Region'


class Languages(models.Model):
    Id = models.AutoField(primary_key=True, verbose_name="language")
    Name = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = 'Language'


class Currencies(models.Model):
    Id = models.AutoField(primary_key=True, verbose_name="currency")
    Name = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = 'Currency'


class Countries(models.Model):
    Id = models.AutoField(primary_key=True, verbose_name="country")
    Name = models.TextField(null=False, blank=False)
    Country_code = models.TextField(null=False, blank=False, unique=True)
    Region = models.ForeignKey(Regions, null=False, blank=False, on_delete=models.CASCADE)
    Language = models.ForeignKey(Languages, null=False, blank=False, on_delete=models.CASCADE)
    Currency = models.ForeignKey(Currencies, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = 'Country'


class Players(models.Model):
    Id = models.AutoField(primary_key=True, null=False, blank=False, verbose_name="player")
    Name = models.TextField(null=False, blank=False)
    Lastname = models.TextField(null=False, blank=False)
    Email = models.EmailField(null=False, blank=False, unique=True)
    Country = models.ForeignKey(Countries, null=False, blank=False, on_delete=models.CASCADE)
    Genre = models.TextField(null=False, blank=False)
    Age = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = 'Player'


class Games(models.Model):
    Id = models.AutoField(primary_key=True, null=False, blank=False, verbose_name="Game")
    Name = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = 'Game'


class Symbols(models.Model):
    Id = models.AutoField(primary_key=True, null=False, blank=False, verbose_name="Symbol")
    Character = models.TextField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.Character

    class Meta:
        verbose_name_plural = 'Symbol'


class Positions(models.Model):
    Id = models.IntegerField(primary_key=True, null=False, blank=False, unique=True, verbose_name="Position")
    Description = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.Id

    class Meta:
        verbose_name_plural = 'Position'

class Matchs(models.Model):
    Id = models.AutoField(primary_key=True, null=False, blank=False, verbose_name="Match")
    Game = models.ForeignKey(Games, null=False, blank=False, on_delete=models.CASCADE)
    Plays = ArrayField(
        models.IntegerField(),
        size = 2
    )
    Moves = ArrayField(
        ArrayField(
            models.IntegerField(),
            size=3
        ),
        size = 9
    )

    def __str__(self):
        return 'Match'

    class Meta:
        verbose_name_plural = 'Match'