from django.db import models


class Region(models.Model):
    Id = models.AutoField(primary_key=True, verbose_name="region")
    name = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Region'


class Language(models.Model):
    Id = models.AutoField(primary_key=True, verbose_name="language")
    name = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Language'


class Currency(models.Model):
    Id = models.AutoField(primary_key=True, verbose_name="currency")
    name = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Currency'


class Country(models.Model):
    Id = models.AutoField(primary_key=True, verbose_name="country")
    name = models.TextField()
    country_code = models.TextField(null=False, blank=False, unique=True)
    regionId = models.ForeignKey(Region, null=False, blank=False, on_delete=models.CASCADE)
    languageId = models.ForeignKey(Language, null=False, blank=False, on_delete=models.CASCADE)
    currencyId = models.TextField()
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Country'


class Player(models.Model):
    Id = models.AutoField(primary_key=True, null=False, blank=False, verbose_name="player")
    name = models.TextField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    password = models.TextField(null=False, blank=False)
    countryId = models.ForeignKey(Country, null=False, blank=False, on_delete=models.CASCADE)
    genre = models.TextField(null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Player'
