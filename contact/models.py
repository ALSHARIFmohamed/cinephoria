
from django.db import models
from users.models import CustomUser

class MessageContact(models.Model):
    utilisateur = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    titre = models.CharField(max_length=255)
    description = models.TextField()
    email = models.EmailField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titre} - {self.email}"

