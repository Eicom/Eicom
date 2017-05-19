from django.conf.urls import include, url
from .import views

urlpatterns = [

    # url(r'^$', views.equipo_list, name='inicio'),
    # url(r'^equipo/(?P<pk>\d+)/$', views.equipo_detalles, name='equipo_detalles'),
    # url(r'^equipos/lista/$/', views.equipo_lista, name='equipo_lista'),
    # url(r'^equipo/nuevo/$', views.equipo_nuevo, name='equipo_nuevo'),
    # url(r'^equipo/(?P<pk>\d+)/edit/$', views.equipo_edit, name='equipo_edit'),
    # url(r'^pruebas/$', views.equipo_pruebas_lista, name='equipo_pruebas_lista'),
    # url(r'^equipo/(?P<pk>\d+)/publish/$', views.equipo_publish, name='equipo_publish'),
    # url(r'^equipo/(?P<pk>\d+)/remove/$', views.equipo_remove, name='equipo_remove'),
    # url(r'^contact/$', views.contact, name='contact'),
    # url(r'^about/$', views.about, name='about'),

    url(r'^$', views.equipo_list, name='inicio'),
    # url(r'^(?P<slug>[\w-]+)/contact/$', views.contact, name='contact'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^pruebas/$', views.pruebas, name='pruebas'),
    # url(r'^create/$', views.equipo_create),
    url(r'^(?P<slug>[\w-]+)/$', views.equipo_detail, name='detail'),
    # url(r'^(?P<slug>[\w-]+)/edit/$', views.equipo_update, name='update'),
    # url(r'^(?P<slug>[\w-]+)/delete/$', views.equipo_delete),
    url(r'^categoria/(?P<filtro>[\w-]+)/$',views.categoria, name='filtro'),

]