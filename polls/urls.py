from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from polls import views

app_name = 'polls'

urlpatterns = [
    url(r'^goto/$', views.tothegallery, name='tothegallery'),
    url(r'^$', views.homepage, name='homepage'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^uploadpic/$', views.uploadPic, name='uploadPic'),
    url(r'^votepage/$', views.votePage, name='votePage'),
    url(r'^vote/(?P<picId>[0-9]+)/$', views.vote, name='vote'),
]
