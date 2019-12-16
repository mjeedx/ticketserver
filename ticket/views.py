from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.utils import timezone
from django.http import JsonResponse
from ticket.forms import Ticket_Form
from ticket.models import Tickets
from django.contrib import auth
from requests import get


send_message = "https://api.telegram.org/bot495013188:AAEXwQcQFFifEpkstwzOafUK7EIDohr-wUI/sendMessage?chat_id=-300176051&text="


# Показ домашней странички с формой ввода тикета
def home_page(request):
    add_form = Ticket_Form
    args = {}
    args.update(csrf(request))
    args['form'] = add_form
    args['username'] = auth.get_user(request).username
    args['url_name'] = request.resolver_match.url_name
    return render_to_response('home.html', args)


# Экшн отправки и сохраненя формы в базу
def send_ticket(request):
    try:
        if request.method == 'POST':
            form = Ticket_Form(request.POST)
            if form.is_valid:
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

                if x_forwarded_for:
                    ip = x_forwarded_for.split(',')[0]
                else:
                    ip = request.META.get('REMOTE_ADDR')
                ticket = form.save(commit=False)
                ticket.ip = ip
                ticket.when = timezone.now()
                ticket.save() # Сохраняем тикет в базу

                message = request.POST.get("who") + " " + \
                          request.POST.get("where") + " " + \
                          request.POST.get("subject")
                get(send_message + message)


    except ObjectDoesNotExist:
        raise Http404
    return HttpResponseRedirect('/tickets/thanks/')
    # data = {"is_taken": "Good"}
    # return JsonResponse(data)


# Админам смотреть список всех заявок
@login_required
def watch_all(request):
    args = {'tickets': Tickets.objects.filter(deleted=False).order_by('-when'),
            'username': auth.get_user(request).username,
            'url_name': request.resolver_match.url_name}
    return render_to_response('watch_all.html', args)


@login_required
def history(request):
    args = {'tickets': Tickets.objects.filter(deleted=True).order_by('-when'),
            'username': auth.get_user(request).username,
            'url_name': request.resolver_match.url_name}
    return render_to_response('history.html', args)


# Смотреть одну заявку
@login_required
def watch_one(request, ticket_id):
    args = {'ticket': Tickets.objects.get(id=ticket_id)}
    return render_to_response('watch_one.html', args)


# Экшн подтверждения выполнения заявки
def confirm(request, ticket_id):
    try:
        selected_ticket = Tickets.objects.get(id=ticket_id)
        if not selected_ticket.finished:
            selected_ticket.finished = True
            selected_ticket.date_end = timezone.now()
            print("test_mark")
        elif selected_ticket.finished:
            selected_ticket.finished = False
            print("test_2")
        selected_ticket.save()
    except ObjectDoesNotExist:
        raise Http404
    return HttpResponseRedirect('/tickets/all/')


# Экшн "удаления" записи
def delete_row(request, ticket_id):
    try:
        selected_ticket = Tickets.objects.get(id=ticket_id)
        selected_ticket.deleted = True
        selected_ticket.save()
    except ObjectDoesNotExist:
        raise Http404
    return HttpResponseRedirect('/tickets/all/')


def test(request):
    count = Tickets.objects.filter(finished=False)
    if count.__len__() >0:
        return JsonResponse({"ok": "ok"})
    else:
        a = {'tickets': "clear"}
        return JsonResponse(a)

