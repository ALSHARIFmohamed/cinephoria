from rest_framework import generics, permissions
from films.models import Film
from seances.models import Seance
from reservations.models import Reservation
from .serializers import FilmSerializer, SeanceSerializer, ReservationSerializer
from rest_framework.permissions import IsAuthenticated

class FilmListAPIView(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class SeanceListAPIView(generics.ListAPIView):
    queryset = Seance.objects.all()
    serializer_class = SeanceSerializer

class ReservationListAPIView(generics.ListAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.filter(utilisateur=self.request.user)
    
    
class ReservationCreateAPIView(generics.CreateAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(utilisateur=self.request.user)
        
        
        
class ReservationDetailAPIView(generics.RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]