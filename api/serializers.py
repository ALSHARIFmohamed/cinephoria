from rest_framework import serializers
from films.models import Film
from seances.models import Seance
from reservations.models import Reservation

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'titre', 'description', 'genre', 'age_minimum', 'affiche']

class SeanceSerializer(serializers.ModelSerializer):
    film = FilmSerializer(read_only=True)

    class Meta:
        model = Seance
        fields = ['id', 'film', 'date', 'heure_debut', 'heure_fin', 'salle', 'qualite']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'seance', 'nb_personnes', 'total', 'date_reservation']
        read_only_fields = ['date_reservation']

