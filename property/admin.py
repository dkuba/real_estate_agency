from django.contrib import admin
from .models import Flat, Complaint, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ["created_at"]
    list_display = ('address', 'price', 'new_building', 'town',
                    'construction_year', 'get_owners')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'has_balcony', 'rooms_number', 'floor')
    raw_id_fields = ("liked_by",)

    def get_owners(self, obj):
        return "\n".join([owner.name for owner in obj.owners.all()])


class ComplaintAdmin(admin.ModelAdmin):
    search_fields = ['user', 'flat__address']
    readonly_fields = ["created_at"]
    list_display = ('user', 'flat', 'message')
    list_filter = ('user', 'flat__address')
    raw_id_fields = ("flat",)


class OwnerAdmin(admin.ModelAdmin):
    search_fields = ['name', ]
    list_display = ('name', 'get_flats')
    list_filter = ('name',)
    raw_id_fields = ("flats",)

    def get_flats(self, obj):
        return "\n".join([str(flat) for flat in obj.flats.all()])


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)

admin.site.register(Owner, OwnerAdmin)
