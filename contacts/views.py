from django.shortcuts import render
from contacts.models import Contacts
from django.shortcuts import render_to_response


def show_contacts(request):
    args = {'contacts': Contacts.objects.all().order_by('family_name')}
    # obj = Contacts.objects.all()
    # arguments = Contacts.objects.get(family_name="Иванов")
    #
    # for a in obj:
    #     print(a.id)
    # print(Contacts.objects)
    # print(obj.count())
    # print(arguments)
    # a = arguments.tel_id
    #
    # print(a)
    # for a in arguments:
    #     print(a)
    return render_to_response('contact.html', args)
