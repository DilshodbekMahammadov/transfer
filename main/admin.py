from django.contrib import admin
from django.utils.html import format_html
from .models import *

class SeasonAdmin(admin.ModelAdmin):
    search_fields = ["name"]

class CountryAdmin(admin.ModelAdmin):
    search_fields = ["name"]

class ClubAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_tag', 'president', 'coach', 'found_date', 'country']
    list_filter = ["country", ]
    search_fields = ['name', 'president', 'coach']
    ordering = ('name', )

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="48" height="48" style="border-radius: 10px;"/>', obj.image.url)
        return "No Image"

    image_tag.short_description = 'Image Preview'

class PlayerAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'age', 'position', 'country', 'price', 'club',]
    list_filter = ['country', 'club', 'position', 'age']
    search_fields = ['name']
    ordering = ('name',)

class TransferAdmin(admin.ModelAdmin):
    list_display = ['player', 'club_from', 'club_to', 'season', 'price', 'price_tft', 'datetime',]
    list_filter = ['player', 'club_from', 'club_to', 'season', 'datetime']
    ordering = ('datetime',)
    search_fields = ['player__name']

admin.site.register(Season, SeasonAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Transfer, TransferAdmin)