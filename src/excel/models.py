from django.db import models


def upload_location(instance, filename):
    return '%s/%s' % (instance.id, filename)


# ***Abilitar los modelos una vez importado el xls
# class Unidade(models.Model):
#     unidad = models.CharField(max_length=10)
#
#     def __str__(self):
#         return self.unidad
#
#
# class Marca(models.Model):
#     marca = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.marca
#
#
# class Modelo(models.Model):
#     Modelo = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.Modelo
#
#
# class Linea(models.Model):
#     linea = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.linea
#
#
# class Familia(models.Model):
#     familia = models.CharField(max_length=200)
#
#     def __str__(self):
#             return self.familia
#
#
# class Divisa(models.Model):
#     divisa = models.CharField(max_length=5)
#
#     def __str__(self):
#             return self.divisa


class Producto(models.Model):
    clave = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)
    unidad = models.CharField(max_length=5, null=False, default='-')
    marca = models.CharField(max_length=100, null=False, default='-')
    modelo = models.CharField(max_length=200, null=False, default='-')
    linea = models.CharField(max_length=200, null=False, default='-')
    familia = models.CharField(max_length=200, null=False, default='-')
    divisa = models.CharField(max_length=5, null=False, default='-')
    #    unidad = models.ForeignKey(Unidade)
    #    marca = models.ForeignKey(Marca)
    #    modelo = models.ForeignKey(Modelo)
    #    linea = models.ForeignKey(Linea)
    #    familia = models.ForeignKey(Familia)
    #    divisa = models.ForeignKey(Divisa)
    precio_pub = models.DecimalField(max_digits=8, decimal_places=2, null=False, default=0)
    imagen = models.ImageField(
        upload_to=upload_location,
        null=True, blank=True,
        height_field='height_field',
        width_field='width_field'
    )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return self.descripcion


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    slug = models.CharField(max_length=10, unique=True,
                            default="question")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
