from django.contrib.auth.decorators import login_required
from urllib.parse import quote_plus
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import Equipo, Categoria, Slideshow
from django.core.mail import send_mail
from django.conf import settings


def equipo_detail(request, slug=None):
    instance = get_object_or_404(Equipo, slug=slug)
    share_string = quote_plus(instance.nombre)
    context = {
        'titulo': 'Detalles',
        'instance': instance,
        'share_string': share_string,
    }
    return render(request, 'equipo_detail.html', context)


def categoria(request, slug):
    categoria_list = Equipo.objects.filter(categoria__slug__icontains=slug)
    queryset_categoria = Categoria.objects.all()
    query = request.GET.get('q')
    if query:
        categoria_list = categoria_list.filter(
            Q(nombre__icontains=query) |
            Q(modelo__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(marca__marca__icontains=query)
        ).distinct()
    paginator = Paginator(categoria_list, 8)  # Show 25 contacts per page
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

    index = queryset.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]

    context = {
        'titulo': slug,
        'object_list': queryset,
        'categorias': queryset_categoria,
        'page_request_var': page_request_var,
        'page_range': page_range,
    }
    return render(request, 'categoria.html', context)


def destacados(request):
    queryset_destacados = Equipo.objects.filter(top_vendido__icontains=1)
    query = request.GET.get('q')
    if query:
        queryset_destacados = queryset_destacados.filter(
            Q(nombre__icontains=query) |
            Q(modelo__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(marca__marca__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_destacados, 8)  # Show 25 contacts per page
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

    index = queryset.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]
    context = {
        'titulo': 'Destacados',
        'object_list': queryset,
        'page_range': page_range,
    }
    return render(request, 'productos_destacados.html', context)


def promociones(request):
    queryset_promocion = Equipo.objects.filter(promo__icontains=1)
    query = request.GET.get('q')
    if query:
        queryset_promocion = queryset_promocion.filter(
            Q(nombre__icontains=query) |
            Q(modelo__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(marca__marca__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_promocion, 8)  # Show 25 contacts per page
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

    index = queryset.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]
    context = {
        'titulo': 'Promociones',
        'object_list': queryset,
        'page_range': page_range,
    }
    return render(request, 'promociones.html', context)


def slideshow_list(request):
    slideshow = Slideshow.objects.all()
    return render(request, 'slideshow.html', {'object_list': slideshow})


def equipo_list(request):
    queryset_equipo = Equipo.objects.all()
    queryset_top_vendidos = Equipo.objects.all().order_by('-id')[:4]
    queryset_slideshow = Slideshow.objects.all()
    query = request.GET.get('q')
    if query:
        queryset_equipo = queryset_equipo.filter(
            Q(nombre__icontains=query) |
            Q(modelo__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(marca__marca__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_equipo, 8)  # Show 25 contacts per page
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

    index = queryset.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]
    context = {
        'titulo': 'Home',
        'object_list': queryset,
        'page_range': page_range,
        'top_vendidos': queryset_top_vendidos,
        'object_slideshow': queryset_slideshow,
        'page_request_var': page_request_var,
    }
    return render(request, 'index.html', context)


def contact(request):
    form = RegContactForm(request.POST or None)
    context = {
        'titulo': 'Contacto',
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
def nuevo(request, var):
    if var == 'pr':
        if request.method == "POST":
            form = RegEquipoForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('start:detail', slug=post.slug)

        else:
             form = RegEquipoForm()
        context = {
            'form': form,
            'titulo': 'Registrar Producto',
        }
        return render(request, 'equipo_form.html', context)

    if var == 'de':
        if request.method == "POST":
            form = RegDepartamentoForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('/')
        else:
            form = RegDepartamentoForm()
        context = {
            'form': form,
            'titulo': 'Registrar Departamento',
        }

    if var == 'ca':
        if request.method == "POST":
            form = RegCategoriaForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('/')
        else:
            form = RegCategoriaForm()
        context = {
            'form': form,
            'titulo': 'Registrar Categoría',
        }

    if var == 'fa':
        if request.method == "POST":
            form = RegFamiliaForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('/')
        else:
            form = RegFamiliaForm()
        context = {
            'form': form,
            'titulo': 'Registrar Familia',
        }

    if var == 'ma':
        if request.method == "POST":
            form = RegMarcaForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('/')
        else:
            form = RegMarcaForm()
        context = {
            'form': form,
            'titulo': 'Registrar Marca',
        }


    if var == 'sl':
        if request.method == "POST":
            form = RegSlideshowForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('/')
        else:
            form = RegSlideshowForm()
            context = {
                'form':form,
                'titulo': 'Registrar Promoción',
            }
    return render(request, 'control_form.html', context)


@login_required
def editar(request, slug):
    post = get_object_or_404(Equipo, slug=slug)
    if request.method == "POST":
        form = RegEquipoForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('start:detail', slug=post.slug)
    else:
        form = RegEquipoForm(instance=post)
    return render(request, 'equipo_form.html', {'form': form})


@login_required
def borrar(request, slug):
    post = get_object_or_404(Equipo, slug=slug)
    post.delete()
    return redirect('start:inicio')


def about(request):
    context = {
        'titulo': 'About us',
    }
    return render(request, 'about.html', context)


def pruebas(request):
    return render(request, 'sitio_en_construccion.html')
