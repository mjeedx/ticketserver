from django import forms
from ticket.models import Tickets


class Ticket_Form(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ('who', 'where', 'subject', 'ip')

class Rocket_user(forms.Form):
    rocket_user = forms.CharField(label="Имя пользователя в чате", max_length=50)

