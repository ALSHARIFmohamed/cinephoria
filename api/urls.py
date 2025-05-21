from django.urls import path
from .views import (
    FilmListAPIView,
    SeanceListAPIView,
    ReservationListAPIView,
    ReservationCreateAPIView,
    ReservationDetailAPIView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('films/', FilmListAPIView.as_view(), name='film-list'),
    path('seances/', SeanceListAPIView.as_view(), name='seance-list'),
    path('reservations/', ReservationListAPIView.as_view(), name='reservation-list'),
    path('reservations/<int:id>/', ReservationDetailAPIView.as_view(), name='reservation-detail'),
    path('reservations/create/', ReservationCreateAPIView.as_view(), name='reservation-create'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]






