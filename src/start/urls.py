from django.conf.urls import include, url
from .import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^$', views.equipo_list, name='inicio'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^pruebas/$', views.pruebas, name='pruebas'),
    url(r'^(?P<slug>[\w-]+)/$', views.equipo_detail, name='detail'),
    url(r'^categoria/(?P<filtro>[\w-]+)/$',views.categoria, name='filtro'),
]
=======

    url(r'^$', views.equipo_list, name='list'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^(?P<slug>[\w-]+)/$', views.equipo_detail, name='detail'),
    url(r'^categoria/(?P<filtro>[\w-]+)/$',views.categoria, name='filtro'),
]

>>>>>>> a2c84bb6414900b317fa31774f5e74fdb247d49f
