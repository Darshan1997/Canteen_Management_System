from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^process', views.payment_process, name='payment_process'),
    url(r'^done', views.payment_done, name='payment_done'),
    url(r'^canceled', views.payment_canceled, name='payment_canceled'),
]