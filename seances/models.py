
from django.db import models
from films.models import Film



class Cinema(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} ({self.ville}, {self.pays})"


class QualiteProjection(models.Model):
    nom = models.CharField(max_length=50)  # ex: 4DX, 3D, 4K
    prix = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.nom} - {self.prix}€"


class Salle(models.Model):
    nom = models.CharField(max_length=100)
    capacite = models.PositiveIntegerField()
    nb_places_handicap = models.PositiveIntegerField(default=0)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)

    qualite = models.ManyToManyField(QualiteProjection)

    def __str__(self):
        return f"{self.nom} - {self.cinema.ville}"



class Seance(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    qualite = models.ForeignKey(QualiteProjection, on_delete=models.CASCADE)
    date = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()

    def __str__(self):
        return f"{self.film.titre} - {self.date} {self.heure_debut}"
