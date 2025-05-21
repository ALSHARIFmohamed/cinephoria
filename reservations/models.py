from django.db import models
from users.models import CustomUser
from seances.models import Seance
from django.utils import timezone

class Reservation(models.Model):
    utilisateur = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    seance = models.ForeignKey(Seance, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField(default=timezone.now)
    nb_personnes = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=6, decimal_places=2)
    validee = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.utilisateur.username} - {self.seance} - {self.total} €"

class Place(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='places')
    numero = models.CharField(max_length=5)
    est_handicap = models.BooleanField(default=False)

    def __str__(self):
        return f"Place {self.numero} ({'PMR' if self.est_handicap else 'Standard'})"
