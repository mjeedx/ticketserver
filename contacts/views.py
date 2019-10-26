from django.shortcuts import render
from contacts.models import Contacts
from django.shortcuts import render_to_response


def show_contacts(request):
    args = {'contacts': Contacts.objects.all().order_by('family_name')}
    return render_to_response('contact.html', args)


