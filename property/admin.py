from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ["created_at"]
    list_display = ('address', 'price', 'new_building', 'town', 'construction_year')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'has_balcony', 'rooms_number', 'floor')


admin.site.register(Flat, FlatAdmin)
