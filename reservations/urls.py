from django.urls import path
from .views import reserver_seance, mes_reservations

urlpatterns = [
    #path('reserver/<int:seance_id>/', reserver_seance, name='reserver_seance'),
    path('mes-reservations/', mes_reservations, name='mes_reservations'),
    path('reservations/reserver/<int:seance_id>/', reserver_seance, name='reserver_seance')

]




