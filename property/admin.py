from django.contrib import admin
from django.contrib.auth.models import User

from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ["created_at"]
    list_display = ('address', 'price', 'new_building', 'town', 'construction_year', 'owner_pure_phone')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'has_balcony', 'rooms_number', 'floor')
    raw_id_fields = ("liked_by",)


class ComplaintAdmin(admin.ModelAdmin):
    search_fields = ['user', 'flat__address']
    readonly_fields = ["created_at"]
    list_display = ('user', 'flat', 'message')
    list_filter = ('user', 'flat__address')
    raw_id_fields = ("flat",)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
