from django.db import models
from seances.models import Salle
from users.models import CustomUser

class Incident(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'À traiter'),
        ('en_cours', 'En cours'),
        ('resolu', 'Résolu'),
    ]

    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    description = models.TextField()
    date_signalement = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    signale_par = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.salle.nom} - {self.statut}"
