"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('clubs/', ClubsView.as_view(), name='clubs'),
    path('clubs/<int:pk>/details/',ClubDetailsView.as_view(), name='club-detail' ),
    path('latest-transfers/', LatestTransfersView.as_view(), name='latest-transfers'),
    path('players/', PlayersView.as_view(), name='players'),
    path('U20-players/', U20PlayersView.as_view(), name='U-20'),
    path('tryouts/', TryoutsView.as_view(), name='tryouts'),
    path('countries/<int:pk>/clubs/', ClubsByCountry.as_view(), name='clubs-by-country'),
    path('top-150-accurate-predictions/', Top150AccuratePredictions.as_view(), name='top-150-accurate-predictions'),
    path('stats/', StatsView.as_view(), name='stats'),
    path('top-50-clubs-by-expenditures/', Top50ClubsByExpendituresView.as_view(), name='top-50-clubs-by-expenditure')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)