from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify


def upload_location(instance, filename):
    return '%s/%s' % (instance.id, filename)


class Departamento(models.Model):
    departamento = models.CharField(max_length=50)

    def __str__(self):
        return self.departamento


class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.categoria


class Marca(models.Model):
    marca = models.CharField(max_length=100)

    def __str__(self):
        return self.marca


class SistemaOperativo(models.Model):
    sistema_operativo = models.CharField(max_length=100)

    def __str__(self):
        return self.sistema_operativo


class Procesador(models.Model):
    procesador = models.CharField(max_length=100)

    def __str__(self):
        return self.procesador


class DiscoDuro(models.Model):
    disco_duro = models.CharField(max_length=100)

    def __str__(self):
        return self.disco_duro


class Ram(models.Model):
    ram = models.CharField(max_length=10)

    def __str__(self):
        return self.ram


class Equipo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    modelo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True)
    sistema_operativo = models.ForeignKey(SistemaOperativo, on_delete=models.SET_NULL, null=True)
    procesador = models.ForeignKey(Procesador, on_delete=models.SET_NULL, null=True)
    disco_duro = models.ForeignKey(DiscoDuro, on_delete=models.SET_NULL, null=True)
    pantalla = models.CharField(max_length=200)
    memoria_ram = models.ForeignKey(Ram, on_delete=models.SET_NULL, null=True)
    bateria = models.CharField(max_length=200, null=True, default='')
    adaptador_ac = models.CharField(max_length=200, null=True, default='')
    camara = models.CharField(max_length=200, null=True, default='')
    tarjeta_madre = models.CharField(max_length=200, null=True, default='')
    video = models.CharField(max_length=200)
    top_vendido = models.BooleanField(default=False)
    promo = models.BooleanField(default=False)
    descripcion = models.TextField(null=True, default='NOT_PROVIDED')
    precio = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    imagen = models.ImageField(
        upload_to=upload_location,
        null=True, blank=True,
        height_field='height_field',
        width_field='width_field'
    )
    imagen_1 = models.ImageField(
        upload_to=upload_location,
        null=True, blank=True,
        height_field='height_field',
        width_field='width_field'
    )
    imagen_2 = models.ImageField(
        upload_to=upload_location,
        null=True, blank=True,
        height_field='height_field',
        width_field='width_field'
    )
    imagen_3 = models.ImageField(
        upload_to=upload_location,
        null=True, blank=True,
        height_field='height_field',
        width_field='width_field'
    )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('start:detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-timestamp']


class Slideshow(models.Model):
    titulo = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    imagen = models.ImageField(upload_to=upload_location, null=True, blank=True,
                               height_field='height_field', width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-timestamp']


class Slideshow_marcas(models.Model):
    titulo = models.CharField(max_length=50, blank=True, null=True)
    imagen = models.ImageField(upload_to=upload_location, null=True, blank=True,
                               height_field='height_field', width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.titulo


def create_slug(instance, new_slug=None):
    slug = slugify(instance.modelo)
    if new_slug is not None:
        slug = new_slug
    qs = Equipo.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_equipo_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


# que se hará con el objeto antes de fguardarlo(slug en éste caso)...
pre_save.connect(pre_save_equipo_receiver, sender=Equipo)


class Mensaje(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField(max_length=300)
    telefono = models.CharField(max_length=15, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.nombre
