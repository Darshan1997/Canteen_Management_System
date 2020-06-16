from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^loginvalidation', views.validation, name='validation'),
    url(r'^registration', views.registration, name='registration'),
    url(r'^register', views.register, name='register'),
    url(r'^choose', views.chooseorder, name='chooseorder'),
    url(r'^addcart', views.addcart, name='addcart'),
    url(r'^removecart', views.removecart, name='removecart'),
    url(r'^placeorder', views.placeorder, name='placeorder'),
    url(r'^qty',views.qty, name='qty'),
    url(r'^confirm',views.confirm, name='confirm'),
    url(r'^history',views.history,name='history'),
    url(r'^viewhistorydetail',views.viewhistorydetail,name='viewhistorydetail'),
    url(r'^forgetpassword',views.forgetpassword,name='forgetpassword'),
    url(r'^fpwd',views.fpwd,name='fpwd'),
    url(r'^changepassword',views.changepassword,name='changepassword'),
    url(r'^cpwd',views.cpwd,name='cpwd'),
    url(r'^getsession',views.getsession,name='getsession'),
    url(r'^cancel',views.cancel,name='cancel'),
    url(r'^logout',views.logout,name='logout'),
    url(r'^uniqueusr',views.uniqueusr,name='uniqueusr'),
    url(r'^category',views.category,name='category'),
    url(r'^ordercancel', views.ordercancel, name='ordercancel'),
    url(r'^editprofilework', views.editprofilework, name='editprofilework'),
    url(r'^editprofile',views.editprofile,name='editprofile'),
    url(r'^searchresult', views.searchresult, name='searchresult'),
]