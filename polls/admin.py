from django.contrib import admin

from polls.models import Img, Category, Users, Likes

admin.site.register(Img),
admin.site.register(Category),
admin.site.register(Users),
admin.site.register(Likes)