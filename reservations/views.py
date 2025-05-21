from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from seances.models import Seance
from .models import Reservation


@login_required
def reserver_seance(request, seance_id):
    seance = get_object_or_404(Seance, pk=seance_id)

    if request.method == "POST":
        nb_personnes = int(request.POST.get("nb_personnes"))
        prix_unitaire = seance.qualite.prix
        total = nb_personnes * prix_unitaire

        Reservation.objects.create(
            utilisateur=request.user,
            seance=seance,
            nb_personnes=nb_personnes,
            total=total,
            validee=True
        )
        return redirect('mes_reservations')  # ou autre

    return render(request, 'reservations/reserver.html', {'seance': seance})








@login_required
def mes_reservations(request):
    reservations = Reservation.objects.filter(utilisateur=request.user).order_by('-date_reservation')
    return render(request, 'reservations/mes_reservations.html', {'reservations': reservations})





