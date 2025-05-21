
from django.urls import path
from . import views

urlpatterns = [
    # exemple de route :
    path('', views.liste_seances, name='liste_seances'),
]

