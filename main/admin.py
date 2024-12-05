from django import forms
from django.contrib import admin
from .models import Table, Guest, Reservation


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('name', 'phone')


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'capacity')
    list_filter = ('capacity',)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date', 'time', 'duration')
    list_filter = ('table', 'date', 'time')
    search_fields = ('guest__name',)
