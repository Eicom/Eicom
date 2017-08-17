from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.equipo_list, name='inicio'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^pruebas/$', views.pruebas, name='pruebas'),
    url(r'^nuevo/$', views.nuevo, name='nuevo'),
    url(r'^detalles/(?P<slug>[\w-]+)/$', views.equipo_detail, name='detail'),
    url(r'^detalles/(?P<slug>[\w-]+)/editar/$', views.editar, name='editar'),
    url(r'^detalles/(?P<slug>[\w-]+)/borrar/$', views.borrar, name='borrar'),
    url(r'^promociones/', views.promociones, name='promo'),
    url(r'^categoria/(?P<slug>[\w-]+)/$', views.categoria, name='categoria'),
]
