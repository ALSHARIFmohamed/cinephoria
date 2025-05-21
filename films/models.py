from django.db import models

class Genre(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Film(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    age_minimum = models.PositiveIntegerField()
    date_ajout = models.DateField(auto_now_add=True)
    coup_de_coeur = models.BooleanField(default=False)
    affiche = models.ImageField(upload_to='affiches/', blank=True, null=True)
    genre = models.ManyToManyField(Genre, related_name='films')

    def __str__(self):
        return self.titre

    def moyenne_notes(self):
        notes = self.avis_set.all()
        if notes:
            return sum(n.note for n in notes) / notes.count()
        return None


class Avis(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    note = models.IntegerField()  # sur 5
    description = models.TextField()
    valide = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.film.titre} - {self.note}/5"
