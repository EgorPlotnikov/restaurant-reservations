from django.db import models

class Table(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return 'Cтол ' + str(self.number)


class Guest(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return str(self.name)


class Reservation(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()

    def __str__(self):
        return str(self.guest) + ' — ' + str(self.table)
