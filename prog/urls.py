from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^adminloginvalidation', views.validation, name='validation'),
    url(r'^adminwork',views.adminwork,name='adminwork'),
    url(r'^additemwork', views.additemwork, name='additemwork'),
    url(r'^additem', views.additem, name='additem'),
    url(r'^addchefwork', views.addchefwork, name='addchefwork'),
    url(r'^addchef', views.addchef, name='addchef'),
    url(r'^viewitem', views.viewitem, name='viewitem'),
    url(r'^viewchef', views.viewchef, name='viewchef'),
    url(r'^vieworder', views.vieworder, name='vieworder'),
    #url(r'^viewdetailwork', views.viewdetailwork, name='viewdetailwork'),
    url(r'^viewdetail', views.viewdetail, name='viewdetail'),
    url(r'^updateitemwork',views.updateitemwork,name='updateitemwork'),
    url(r'^updatechefwork',views.updatechefwork,name='updatechefwork'),
    url(r'^deletechef',views.deletechef,name='deletechef'),
    url(r'^updatechef',views.updatechef,name='updatechef'),
    url(r'^deleteitem',views.deleteitem,name='deleteitem'),
    url(r'^updateitem',views.updateitem,name='updateitem'),
    url(r'^forget',views.forget,name='forget'),
    url(r'^fp',views.fp,name='fp'),
    url(r'^logout',views.logout,name='logout'),
    url(r'^uniqueino', views.uniqueino, name='uniqueino'),
    url(r'^uniquecid', views.uniquecid, name='uniquecid'),
    url(r'^viewcustomer',views.viewcustomer,name='viewcustomer'),
    url(r'^searchresult', views.searchresult, name='searchresult'),

]