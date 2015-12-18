from django.conf.urls import patterns, url 
from . import views
urlpatterns = [
# handling menu urls
    url(r'^home/$', views.home_list, name='home_list'),
    url(r'^contact/$', views.email, name='email'),
    url(r'^index/', views.index_list, name='index_list'),
    url(r'^$', views.home_list, name='home_list'),
    url(r'^gallery/$', views.index_li, name='index_li'),
   
    url(r'^gallery/$', views.index_li, name='index_li'),

    #url(r'^restricted/', views.restricted, name='restricted'),

    url(r'^login/$',
    	 'django.contrib.auth.views.login',
        name='login',
        kwargs={'template_name': 'wedding/login.html'}),

    
    url(r'^about/$', views.about, name='about'),
    url(r'^blog/$', views.blog, name='blog'),
   
# hadling after mail post rutine
    url(r'^thanks/$',
        views.thanks,
        name='thanks'
        ),
#this handles login 


    



]