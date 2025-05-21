from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('films/', views.liste_films, name='liste_films'),
    path('films/<int:film_id>/', views.detail_film, name='detail_film'),
    path('films/<int:film_id>/seances/', views.liste_seances, name='liste_seances'),
]

