from django.contrib import admin

from carts.models import Cartridge, Events, Place, Status, Modell, Num

admin.site.register(Cartridge),
admin.site.register(Events),
admin.site.register(Place),
admin.site.register(Status),
admin.site.register(Modell),
admin.site.register(Num)
