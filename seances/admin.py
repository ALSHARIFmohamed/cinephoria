

# Register your models here.
from django.contrib import admin
from .models import Salle, QualiteProjection, Seance,Cinema
admin.site.register(Cinema)
admin.site.register(Salle)
admin.site.register(QualiteProjection)
admin.site.register(Seance)
