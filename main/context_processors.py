from .models import *

def countries_list(request):
    countries = Country.objects.all()
    c = countries
    for country in countries:
        if not country .club_set.all().exists():
            c = c.exclude(id=country.id)

    l = len(c)
    if l % 2 == 1:
        country_left = c[:l // 2 +1]
        country_right = c[l // 2 +1:]
    else:
        country_left = c[:l // 2]
        country_right = c[l // 2:]
    return {'country_left' : country_left, 'country_right': country_right}
