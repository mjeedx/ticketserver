from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.contrib import auth

from ticket.models import Tickets


def main(request):
    args = {}
    args['username'] = auth.get_user(request).username
    args['url_name'] = request.resolver_match.url_name
    args['new_tickets'] = len(Tickets.objects.filter(confirmed=False))  # к-во незавершенных заявок
    args['not_finished'] = len(Tickets.objects.filter(finished=False))  # к-во незавершенных заявок
    return render_to_response("main.html", args)


def you_tube(request):
    return render_to_response("you_tube.html")
