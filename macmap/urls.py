from django.conf.urls import url
import pysnmp
from macmap import views

app_name = 'macmap'

urlpatterns = [
    url(r'^mac_request/$', views.mac_request, name='mac_request'),
    url(r'^macmap/$', views.macmap, name='macmap')
]