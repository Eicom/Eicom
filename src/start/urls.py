from django.conf.urls import include, url
from .import views

urlpatterns = [

    url(r'^$', views.equipo_list, name='list'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^(?P<slug>[\w-]+)/$', views.equipo_detail, name='detail'),
    url(r'^categoria/(?P<filtro>[\w-]+)/$',views.categoria, name='filtro'),
]
