

# Register your models here.
from django.contrib import admin
from .models import Reservation, Place

class PlaceInline(admin.TabularInline):
    model = Place
    extra = 0

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['utilisateur', 'seance', 'total', 'validee']
    inlines = [PlaceInline]

admin.site.register(Reservation, ReservationAdmin)
