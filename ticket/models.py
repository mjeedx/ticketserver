from django.db import models


class Tickets(models.Model):
    who = models.CharField(max_length=150)
    subject = models.TextField()
    where = models.CharField(max_length=200)
    when = models.DateTimeField(auto_now=False)
    date_end = models.DateTimeField(auto_now=False, null=True)
    confirmed = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    ip = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.who
