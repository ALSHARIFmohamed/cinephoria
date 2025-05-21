from django.shortcuts import render, get_object_or_404
from films.models import Film
from seances.models import Seance

# Accueil du site (derniers films)
def accueil(request):
    films = Film.objects.order_by('-date_ajout')[:5]
    return render(request, 'films/accueil.html', {'films': films})

# Tous les films
def liste_films(request):
    films = Film.objects.all()
    return render(request, 'films/liste_films.html', {'films': films})

# Détail d'un film (titre, description, note...)
def detail_film(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    return render(request, 'films/detail_film.html', {'film': film})



# Séances d’un film
def liste_seances(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    seances = Seance.objects.filter(film=film).order_by('date', 'heure_debut')
    return render(request, 'films/liste_seances.html', {'film': film, 'seances': seances})

