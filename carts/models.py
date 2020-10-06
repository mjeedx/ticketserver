from django.db import models
# from django.utils import timezone


class Modell(models.Model):
    modell = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return str(self.modell)


class Num(models.Model):
    num = models.IntegerField(unique=True)
    modell = models.ForeignKey(Modell, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.num)


class Status(models.Model):
    status = models.CharField(max_length=25)

    def __str__(self):
        return str(self.status)


class Place(models.Model):
    place = models.CharField(max_length=40)

    def __str__(self):
        return str(self.place)


class Cartridge(models.Model):
    num = models.ForeignKey(Num, on_delete=models.PROTECT)
    fill_count = models.IntegerField(default=0)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    place = models.ForeignKey(Place, on_delete=models.PROTECT)
    last_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.num)


class Events(models.Model):
    date = models.DateTimeField(auto_now=True)
    num = models.ForeignKey(Num, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, default=1, on_delete=models.PROTECT)
    place = models.ForeignKey(Place, on_delete=models.PROTECT)
    comment = models.TextField(max_length=200, blank=True)
    deleted = models.BooleanField(default=False)

#    class Meta:
#        get_latest_by = "date"
    def __str__(self):
        return str(self.status)
