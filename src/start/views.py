from django.contrib.auth.decorators import login_required
from urllib.parse import quote_plus
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegContactForm, RegEquipoForm
from .models import Equipo, Categoria, Slideshow
from django.core.mail import send_mail
from django.conf import settings


def equipo_detail(request, slug=None):
    instance = get_object_or_404(Equipo, slug=slug)
    share_string = quote_plus(instance.nombre)
    context = {
        'titulo': instance.nombre,
        'instance': instance,
        'share_string': share_string,
    }
    return render(request, 'equipo_detail.html', context)


def promociones(request):
    queryset = Equipo.objects.all()
    context = {
        'object_list': queryset,
    }
    return render(request, 'promociones.html', context)


def categoria(request, slug):
    queryset_list_2 = Equipo.objects.filter(categoria__slug__icontains=slug)
    queryset_categoria_2 = Categoria.objects.all()
    query_2 = request.GET.get('q')
    if query_2:
        queryset_list_2 = queryset_list_2.filter(
            Q(nombre__icontains=query_2) |
            Q(modelo__icontains=query_2)
        ).distinct()
    paginator = Paginator(queryset_list_2, 16)  # Show 25 contacts per page
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
        'object_clasificacion': queryset_categoria_2,
        # 'page_request_var': page_request_var,
    }
    return render(request, 'categoria.html', context)


def slideshow_list(request):
    slideshow = Slideshow.objects.all()
    return render(request, 'slideshow.html', {'object_list': slideshow})


def equipo_list(request):
    queryset_list = Equipo.objects.all()
    queryset_categoria = Categoria.objects.all()
    queryset_slideshow = Slideshow.objects.all()
    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
            Q(nombre__icontains=query) |
            Q(modelo__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(marca__marca__icontains=query)
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
        'object_clasificacion': queryset_categoria,
        'object_slideshow': queryset_slideshow,
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
        # form_telefono = form.cleaned_data.get('telefono')
        # form_tema = form.cleaned_data.get('tema')
        form_mensaje = form.cleaned_data.get('mensaje')
        asunto = 'Form de Contacto'
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, 'eicomtecnologias@gmail.com']
        email_mensaje = '%s: %s enviado por %s' % (form_nombre, form_mensaje, form_email)
        if not instance.nombre:
            instance.nombre = 'Persona'
        instance.save()

        context = {
            'titulo': 'Gracias %s, tu mensaje ha sido enviado!' % (form_nombre)
        }
        if not form_nombre:
            context = {
                'titulo': 'Gracias %s, tu mensaje ha sido enviado!' % (form_email)
            }

        send_mail(
            asunto,
            email_mensaje,
            email_from,
            email_to,
            fail_silently=False
                  )
        return redirect('/')

    return render(request, 'contact.html', context)


@login_required
def nuevo(request):
    if request.method == "POST":
        form = RegEquipoForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('start:detail', slug=post.clave.lower())
    else:
        form = RegEquipoForm()
    return render(request, 'equipo_form.html', {'form': form})


@login_required
def editar(request, slug):
    post = get_object_or_404(Equipo, slug=slug)
    if request.method == "POST":
        form = RegEquipoForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('start:detail', slug=post.slug.lower())
    else:
        form = RegEquipoForm(instance=post)
    return render(request, 'equipo_form.html', {'form': form})


@login_required
def borrar(request, slug):
    post = get_object_or_404(Equipo, slug=slug)
    post.delete()
    return redirect('start:inicio')


def about(request):
    return render(request, 'about.html')


def pruebas(request):
    return render(request, 'sitio_en_construccion.html')
