from urllib.parse import quote_plus
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegEquipoForm, RegContactForm, RegCategoriaForm, RegSlideshowForm, RegSlideshowMarcasForm
from .models import Equipo, Mensaje, Categoria, Slideshow, Slideshow_marcas
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def equipo_detail(request, slug=None):
    instance = Equipo.objects.get(id=1)
    instance = get_object_or_404(Equipo, slug=slug)
    share_string = quote_plus(instance.nombre)
    context = {
        'titulo': instance.nombre,
        'instance': instance,
        'share_string': share_string,
    }
    return render(request, 'equipo_detail.html', context)

def categoria(request,filtro):
    queryset_list_2 = Equipo.objects.filter(categoria__categoria__icontains=filtro)
    queryset_categoria_2 = Categoria.objects.all()
    query_2 = request.GET.get('q')
    if query_2:
        queryset_list_2 = queryset_list_2.filter(
            Q(nombre__icontains=query_2) |
            Q(modelo__icontains=query_2) |
            Q(marca__icontains=query_2)
        ).distinct()
    paginator = Paginator(queryset_list_2, 8)  # Show 25 contacts per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var, 1)
    try:
        queryset_2 = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset_2 = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset_2 = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset_2,
        'titulo': 'List',
        # 'object_list': queryset_2,
        'object_clasificacion': queryset_categoria_2,
        'page_request_var': page_request_var,
    }
    return render(request, 'categoria.html', context)


def slideshow_list(request):
	slideshow = Slideshow.objects.all()
	return render(request,'slideshow.html',{'object_list':slideshow})

def slideshow_marcas(request):
	slideshow_mr = Slideshow_marcas.objects.all()
	return render(request,'marcas.html',{'object_list':slideshow_mr})

def equipo_list(request):
    queryset_list = Equipo.objects.all()
    queryset_categoria = Categoria.objects.all()
    queryset_slideshow = Slideshow.objects.all()
    queryset_slideshow_marcas = Slideshow_marcas.objects.all()
    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
            Q(nombre__icontains=query) |
            Q(modelo__icontains=query) |
            Q(marca__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 8)  # Show 25 contacts per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var, 1)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        'titulo': 'List',
        'object_list': queryset,
        'object_clasificacion':queryset_categoria,
        'object_slideshow': queryset_slideshow,
        'object_slideshow_marcas': queryset_slideshow_marcas,
        'page_request_var': page_request_var,
    }
    return render(request, 'index.html', context)

def contact(request):
    titulo = 'Contacto'
    form = RegContactForm(request.POST or None)
    context = {
        'titulo': titulo,
        'contact_form': form,
    }
    if form.is_valid():
        instance = form.save(commit=False)
        form_nombre = form.cleaned_data.get('nombre')
        form_email = form.cleaned_data.get('email')
        form_telefono = form.cleaned_data.get('telefono')
        # form_tema = form.cleaned_data.get('tema')
        form_mensaje = form.cleaned_data.get('mensaje')
        asunto = 'Form de Contacto'
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, 'neros.anm@gmail.com']
        email_mensaje = '%s: %s enviado por %s' %(form_nombre, form_mensaje, form_email)
        if not instance.nombre:
            instance.nombre = 'Persona'
        instance.save()

        context = {
            'titulo': 'Gracias %s, tu mensaje ha sido enviado!' %(form_nombre)
        }
        if not form_nombre:
            context = {
                'titulo': 'Gracias %s, tu mensaje ha sido enviado!' %(form_email)
            }

        send_mail(
            asunto,
            email_mensaje,
            email_from,
            email_to,
            fail_silently=False
                  )

    return render(request, 'contact.html', context)

def about(request):
    return render(request,'about.html')

def pruebas(request):
    return render(request,'sitio_en_construccion.html')