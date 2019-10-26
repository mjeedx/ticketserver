from django.forms import ModelForm
from ticket.models import Tickets


class Ticket_Form(ModelForm):
    class Meta:
        model = Tickets
        fields = ('who', 'where', 'subject', 'ip')

