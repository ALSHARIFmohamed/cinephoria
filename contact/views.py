from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import MessageContact

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            if request.user.is_authenticated:
                message.utilisateur = request.user  
            message.save()
            messages.success(request, "Votre message a été envoyé avec succès.")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})



