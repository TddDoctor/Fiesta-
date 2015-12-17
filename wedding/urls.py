from django.conf.urls import patterns, url 
from . import views
urlpatterns = [
    url(r'^home/$', views.home_list, name='home_list'),
    url(r'^contact/$', views.email, name='email'),
    url(r'^index/', views.index_list, name='index_list'),
    url(r'^$', views.home_list, name='home_list'),
    url(r'^gallery/$', views.index_li, name='index_li'),
    
    url(r'^about/$', views.about, name='about'),
    url(r'^blog/$', views.blog, name='blog'),
   
    
    url(r'^thanks/$',
        views.thanks,
        name='thanks'
        ),

    



]