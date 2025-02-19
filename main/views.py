from django.db.models import ExpressionWrapper, FloatField, F, Func, Sum
from django.shortcuts import render, get_object_or_404
from django.views import View
from main.models import *

class HomePageView(View):
    def get(self, request):
        return render(request, 'index.html')

class ClubsView(View):
    def get(self, request):
        clubs = Club.objects.all()
        context = {
            'clubs' : clubs
        }
        return render(request, 'clubs.html', context)

class ClubDetailsView(View):
    def get(self, request, pk):
        club = get_object_or_404(Club, pk=pk)
        players = club.player_set.order_by('-price')
        context = {
            'club': club,
            'players': players
        }
        return render(request, 'club-details.html', context)

class LatestTransfersView(View):
    def get(self, request):
        transfers = Transfer.objects.order_by('-datetime')
        context = {
            'transfers' : transfers,
        }
        return render(request, 'latest-transfers.html', context)

class PlayersView(View):
    def get(self, request):
        players = Player.objects.order_by('-price')
        context = {
            'players' : players,
        }
        return render(request, 'players.html', context)

class U20PlayersView(View):
    def get(self, request):
        players = Player.objects.filter(age__lt=20)
        context = {
                'players' : players,
        }
        return render(request, 'U20-players.html', context)

class TryoutsView(View):
    def get(self, request):
        return render(request, 'tryouts.html')

class ClubsByCountry(View):
    def get(self, request, pk):
        country = get_object_or_404(Country, pk=pk)
        clubs = country.club_set.all()
        context = {
            'clubs': clubs,
            'country' : country,
        }
        return render(request, 'clubs-by-country.html', context)

class Top150AccuratePredictions(View):
    def get(self, request):
        transfers = Transfer.objects.annotate(
            price_difference=Func(
                F('price') - F('price_tft'),
                function='ABS',
                output_field=FloatField()
            )
        ).order_by('price_difference')
        context = {
            'transfers' : transfers,
        }
        return render(request, 'stats/150-accurate-predictions.html', context)

class StatsView(View):
    def get(self, request):
        return render(request, 'stats.html')

class Top50ClubsByExpendituresView(View):
    def get(self, request):
        clubs_by_expenditure = (
            Transfer.objects.values("club_to__name")
            .annotate(total_expenditure=Sum("price"))
            .order_by("-total_expenditure")[:50]
        )

        context = {"clubs_by_expenditure": clubs_by_expenditure}
        return render(request, "stats/top-50-clubs-by-expenditure-in-2021.html", context)