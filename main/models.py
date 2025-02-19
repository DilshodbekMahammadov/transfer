from platform import release

from django.db import models
from django.core.validators import MinValueValidator

class Season(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='clubs/')
    president = models.CharField(max_length=255, blank=True, null=True)
    coach = models.CharField(max_length=255, blank=True, null=True)
    found_date = models.DateField(blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()
    position = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    price = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0)])
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    club_from = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='club_from_set')
    club_to = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='club_to_set')
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    price_tft = models.FloatField(validators=[MinValueValidator(0.0)], blank=True, null=True)
    datetime = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.player} | {self.club_from} - {self.club_to}"







