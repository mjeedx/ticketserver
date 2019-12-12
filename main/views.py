from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.contrib import auth


def main(request):
    args = {}
    args['username'] = auth.get_user(request).username
    args['url_name'] = request.resolver_match.url_name
    return render_to_response("main.html", args)
