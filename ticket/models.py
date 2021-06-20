from django.db import models


class Tickets(models.Model):
    who = models.CharField(max_length=150)
    subject = models.TextField()
    where = models.CharField(max_length=200)
    when = models.DateTimeField(auto_now=False)  # Date when ticket was created
    date_end = models.DateTimeField(auto_now=False, null=True)  # Date when ticket is done
    date_confirm = models.DateTimeField(auto_now=False, null=True) # Date of confirmation
    confirmed = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    ip = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.who
