from django.contrib import admin

from contacts.models import Company, Position, Mail, Tel, Department, Location, Contacts

admin.site.register(Company),
admin.site.register(Position),
admin.site.register(Mail),
admin.site.register(Tel),
admin.site.register(Department),
admin.site.register(Location),
admin.site.register(Contacts)