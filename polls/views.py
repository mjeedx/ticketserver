from django.contrib import auth
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf

from polls.forms import UploadForm
from polls.models import Img, Likes, User

land = 1
humor = 3
other = 4


def tothegallery(request):
    args = {'username': auth.get_user(request).username}
    return render_to_response('ToTheGallery.html', args)


def homepage(request):
    args = {'landscape': Img.objects.filter(categoryId=land)}
    args['humor'] = Img.objects.filter(categoryId=humor)
    args['other'] = Img.objects.filter(categoryId=other)
    args['username'] = auth.get_user(request).username
    return render_to_response('albums.html', args)


@login_required
def upload(request):
    uId = auth.get_user(request).id
    args = {}
    args.update(csrf(request))
    args['form'] = UploadForm(initial={'userId': 1})
    args['photoLast'] = 999 - len(Img.objects.filter(userId=uId))
    args['username'] = auth.get_user(request).username
    return render_to_response('upload.html', args)


@login_required
def uploadPic(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            uId = auth.get_user(request).id
            photoCount = Img.objects.filter(userId=uId)
            if photoCount.__len__() <= 999:
                form.instance.userId_id = uId
                upload = form.save(commit=False)
                ip = 4
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                if x_forwarded_for:
                    ip = x_forwarded_for.split(',')[0]
                else:
                    ip = request.META.get('REMOTE_ADDR')
                upload.ip = ip
                upload.save()
    return HttpResponseRedirect('/polls/')


def votePage(request):
    uId = auth.get_user(request).id
    args = {'pics': Img.objects.all()}
    args['likesLast'] = 9 - len(Likes.objects.filter(userId=uId))
    return render_to_response('votepage.html', args)


def vote(request, picId):
    if auth.get_user(request).is_authenticated:
        user = User.objects.get(id=auth.get_user(request).id)
        img = Img.objects.get(id=picId)
        if not User.objects.get(id=img.userId_id).id == user.id:
            try:
                Likes.objects.get(userId=user, imgId=img)
                return HttpResponseRedirect('/polls/votepage/')
            except:
                cnt = Likes.objects.filter(userId=user).__len__()
                if cnt < 9:
                    like = Likes(userId=user, imgId=img)
                    like.save()
                    lk = Img.objects.get(id=picId)
                    lk.like += 1
                    lk.save()
    if not auth.get_user(request).is_authenticated:
        return HttpResponseRedirect('/accounts/login/')
    return HttpResponseRedirect('/polls/votepage/')
