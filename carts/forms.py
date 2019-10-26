from django import forms
from django.forms import ModelForm


from carts.models import Events, Place, Cartridge


class Events_form(ModelForm):

    # place = forms.ModelChoiceField(queryset=Place.objects.all(),

    class Meta:
        model = Cartridge
        fields = ('num', 'status', 'place')


class Group_ops_form(forms.Form):
    nums = forms.CharField(label="nums", max_length=150)
