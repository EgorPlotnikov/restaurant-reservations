from django.http import HttpResponse
from django.shortcuts import render, redirect

from main.models import Table, Guest, Reservation


def guest(request):
    return render(request, 'guest.html')


def reservation(request):
    tables = Table.objects.all()
    this_guest = Guest.objects.last()
    reservations = Reservation.objects.all()
    return render(request, 'reservation.html',
                  {'tables': tables, 'this_guest': this_guest,
                   'reservations': reservations})


def postguest(request):
    name = request.POST.get('name', 'Unknown')
    phone = request.POST.get('phone', 'Unknown')
    new_guest = Guest.objects.create(name=name, phone=phone)
    return redirect('/reservation')


def postreservation(request):
    this_guest = Guest.objects.last()
    table_number = request.POST.get('table_number', 'Unknown')
    table = Table.objects.get(number=table_number)
    date = request.POST.get('date', 'Unknown')
    time = request.POST.get('time', 'Unknown')
    duration = request.POST.get('duration', 'Unknown')
    new_reservation = Reservation.objects.create(guest=this_guest, table=table,
                                                 date=date, time=time, duration=duration)
    return HttpResponse(str(new_reservation.guest) + ' — ' + str(new_reservation.table)
                        + ' — ' + str(new_reservation.date) + ' — ' + str(new_reservation.time)
                        + ' — ' + str(new_reservation.duration) + ' часа')
