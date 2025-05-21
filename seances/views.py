from django.shortcuts import render, get_object_or_404
from films.models import Film
from .models import Seance

def liste_seances(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    seances = Seance.objects.filter(film=film)
    return render(request, 'seances/liste_seances.html', {'film': film, 'seances': seances})

