from django import forms
from .models import MessageContact



class ContactForm(forms.ModelForm):
    class Meta:
        model = MessageContact
        fields = ['titre', 'description']  
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
