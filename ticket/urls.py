from django.conf.urls import url
from django.views.generic import TemplateView

from ticket import views

app_name = 'ticket'

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^thanks/$', TemplateView.as_view(template_name="thanks.html")),
    url(r'^test/$', views.test, name='test'),
    url(r'^delete_row/(?P<ticket_id>[0-9]+)/$', views.delete_row, name='delete_row'),
    url(r'^all/$', views.watch_all, name='watch_all'),
    url(r'^my_tickets/$', views.my_tickets, name='my_tickets'),
    url(r'^watch/(?P<ticket_id>[0-9]+)/$', views.watch_one, name='watch_one'),
    url(r'^history/$', views.history, name='history'),
    url(r'^ticket_add/$', views.send_ticket, name='ticket_add'),
    url(r'^finish/(?P<ticket_id>[0-9]+)/$', views.finish, name='finish'),
    url(r'^confirm/(?P<ticket_id>[0-9]+)/$', views.confirm, name='confirm'),
]