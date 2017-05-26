from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.

<<<<<<< HEAD


=======
>>>>>>> a2c84bb6414900b317fa31774f5e74fdb247d49f
def upload_location(instance, filename):
    return '%s/%s' % (instance.id, filename)

class Categoria(models.Model):
<<<<<<< HEAD
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria
=======
	categoria = models.CharField(max_length=50)

	def __str__(self):
		return self.categoria
>>>>>>> a2c84bb6414900b317fa31774f5e74fdb247d49f

class Equipo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    modelo = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
<<<<<<< HEAD
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    so = models.CharField(max_length=50, default='None')
    marca = models.CharField(max_length=50)
    procesador = models.CharField(max_length=50)
    harddrive = models.CharField(max_length=50)
    pantalla = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    video = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField (max_digits=8, decimal_places=2, null=False)
=======
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    so = models.CharField(max_length=50,default='None')
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    procesador = models.CharField(max_length=50)
    harddrive = models.CharField(max_length=50)
    pantalla = models.CharField(max_length=50,null=True,blank=True,default='-')
    ram = models.CharField(max_length=50)
    video = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
>>>>>>> a2c84bb6414900b317fa31774f5e74fdb247d49f
    imagen = models.ImageField(
        upload_to=upload_location,
        null=True, blank=True,
        height_field='height_field',
        width_field='width_field'
    )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
<<<<<<< HEAD
        return self.modelo
=======
        return self.nombre
>>>>>>> a2c84bb6414900b317fa31774f5e74fdb247d49f

    def get_absolute_url(self):
        return reverse('start:detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-timestamp']

<<<<<<< HEAD
class Slideshow(models.Model):
	titulo = models.CharField(max_length=50,blank=True,null=True)
	descripcion = models.CharField(max_length=150,blank=True,null=True)
	equipo = models.ForeignKey(Equipo,on_delete=models.CASCADE,null=True,blank=True)
	imagen = models.ImageField(upload_to=upload_location,null=True,blank=True,height_field='height_field',width_field='width_field')
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)

	def __str__(self):
		return self.titulo

	class Meta:
		ordering = ['-timestamp']

=======
>>>>>>> a2c84bb6414900b317fa31774f5e74fdb247d49f

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

#que se hará con el objeto antes de fguardarlo(slug en éste caso)...
pre_save.connect(pre_save_equipo_receiver, sender=Equipo)

class Mensaje(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
<<<<<<< HEAD
    asunto= models.CharField(max_length=50)
    mensaje = models.TextField(max_length=300)
=======
    tema = models.CharField(max_length=50)
    mensaje = models.TextField()
>>>>>>> a2c84bb6414900b317fa31774f5e74fdb247d49f
    telefono = models.CharField(max_length=15, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.nombre
