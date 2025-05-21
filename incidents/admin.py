from django.contrib import admin
from .models import Incident

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ['salle', 'statut', 'date_signalement']
    list_filter = ['statut', 'salle']
    search_fields = ['description']

