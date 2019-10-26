from django.conf.urls import url
from django.views.generic import TemplateView

from contacts import views

#app_name = 'contacts'

urlpatterns = [
    url(r'^$', views.show_contacts, name='show_contacts'),

]
