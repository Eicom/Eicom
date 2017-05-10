from urllib.parse import quote_plus
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegEquipoForm, RegContactForm
from .models import Equipo, Mensaje
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

# def equipo_create(request):
#     if not request.user.is_staff or not request.user.is_superuser:
#         raise Http404
#     form = RegEquipoForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.user = request.user
#         #False en caso de que se añadan condiciones previas al guardado
#         instance.save()
#         messages.success(request, 'El registro ha sido guardado correctamente')
#         return HttpResponseRedirect(instance.get_absolute_url())
#     context = {
#         'form': form
#     }
#     return render(request, 'equipo_form.html', context)

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

def equipo_list(request):
    queryset_list = Equipo.objects.all()
    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
            Q(clasificacion__icontains=query)|
            Q(nombre__icontains=query)|
            Q(modelo__icontains=query) |
            Q(marca__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 12)  # Show 25 contacts per page
    page_request_var = 'list'
    page = request.GET.get(page_request_var)
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
        'page_request_var': page_request_var,
    }
    return render(request, 'index.html', context)

# def equipo_update(request, slug=None):
#     if not request.user.is_staff or not request.user.is_superuser:
#         raise Http404
#     instance = get_object_or_404(Equipo, slug=slug)
#     form = RegEquipoForm(request.POST or None, request.FILES or None, instance=instance)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#         messages.success(request, 'El <a href="#">registro</a> ha sido modificado correctamente', extra_tags='html_safe')
#         return HttpResponseRedirect(instance.get_absolute_url())
#     context = {
#         'titulo': instance.nombre,
#         'instance': instance,
#         'form': form,
#     }
#     return render(request, 'equipo_form.html', context)

# def equipo_delete(request, slug=None):
#     if not request.user.is_staff or not request.user.is_superuser:
#         raise Http404
#     instance = get_object_or_404(Equipo, slug=slug)
#     instance.delete()
#     messages.success(request, 'El registro ha sido elimiando correctamente')
#     return redirect('start:list')

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
        form_tema = form.cleaned_data.get('tema')
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