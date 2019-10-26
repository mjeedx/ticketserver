from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm



def login(request):
    args = {}
    args.update(csrf(request))
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('/polls')
    else:
        args['login_error'] = "Пользователь не найден"
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/tickets/")

def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newUserForm = UserCreationForm(request.POST)
        if newUserForm.is_valid():
            newUserForm.save()
            newuser = auth.authenticate(username=newUserForm.cleaned_data['username'],
                                        password=newUserForm.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/polls/')
        else:
            args['form'] = newUserForm
    return render_to_response('register.html', args)
