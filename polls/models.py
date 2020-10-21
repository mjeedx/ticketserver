from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import get_thumbnail


class Users(User):
    dept = models.CharField(max_length=35, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)

    # def __str__(self):
    #     return str(self.name)


class Category(models.Model):
    category = models.CharField(max_length=25)

    def __str__(self):
        return str(self.category)


class Img(models.Model):
    title = models.CharField(max_length=100)
    userId = models.ForeignKey(User, on_delete=models.PROTECT)
    categoryId = models.ForeignKey(Category, on_delete=models.PROTECT)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    ip = models.CharField(max_length=30, null=True, blank=True)
    like = models.IntegerField(default=0)

    def __str__(self):
        return str(self.title)

    def get_image_200x200(self):
        return get_thumbnail(self.photo, '200x200', crop='center')


class Likes(models.Model):
    userId = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT)
    imgId = models.ForeignKey(Img, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.userId)
