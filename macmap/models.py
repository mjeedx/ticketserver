from django.db import models


class Sw_db(models.Model): # БД свитчей
    vendor = models.CharField(max_length=25)
    model = models.CharField(max_length=30)
    region = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    ipv4 = models.CharField(max_length=15)
    enable = models.BooleanField(default=True)
    name = models.CharField(max_length=35, blank=True)

    def __str__(self):
        return str(self.ipv4)


class Mac_list(models.Model): # Полученные данные со свитчей
    sw_id = models.ForeignKey(Sw_db, on_delete=models.PROTECT)
    port = models.CharField(max_length=7)
    mac = models.CharField(max_length=17)
    time = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.mac)
