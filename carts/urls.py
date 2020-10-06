from django.conf.urls import url
from django.views.generic import TemplateView

from carts import views

app_name = 'cart'

urlpatterns = [
    url(r'^cart_home/$', views.home, name='cart_home'),
    url(r'^event_add/$', views.event_add, name='event_add'),
    # url(r'^watch_one_num/(?P<num_id>[0-9]+)/$', views.watch_one_num, name='watch_one_num'),
    url(r'^watch_one_num/(?P<num_id>[0-9]+)/$', views.watch_one_num, name='watch_one_num'),
    url(r'^watch_status/(?P<status_id>[0-9]+)/$', views.watch_status, name='watch_status'),
    url(r'^watch_place/(?P<place_id>[0-9]+)/$', views.watch_place, name='watch_place'),
    url(r'^watch_model/(?P<model_id>[0-9]+)/$', views.watch_model, name='watch_model'),
    url(r'^homecoming/(?P<num_id>[0-9]+)/$', views.homecoming, name='homecoming'),
    url(r'^send_refill/(?P<num_id>[0-9]+)/$', views.send_refill, name='send_refill'),
    url(r'^test/$', TemplateView.as_view(template_name="test.html")),
    url(r'^cart_home/group_ops/$', views.group_ops, name='group_ops'),
    url(r'^cart_home/get_group_ops/$', views.get_group_ops, name='get_group_ops'),
    url(r'^cart_home/get_swap/$', views.get_swap, name='get_swap'),
    # url(r'^cart_home/get_swap/(?P<num>[0-9]+)/$', views.get_swap, name='get_swap'),
]
