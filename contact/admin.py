
from django.contrib import admin
from .models import MessageContact

@admin.register(MessageContact)
class MessageContactAdmin(admin.ModelAdmin):
    list_display = ['titre', 'email', 'date_envoi']
    search_fields = ['titre', 'email']
