from django.db import models

# Create your models here.
class Lector(models.Model):
	grupos = (
		("est", "Estudiante"), 
		("doc", "Docente")
	)
	id_lector = models.CharField(primary_key=True, max_length=8)
	nombres = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)
	telefono = models.CharField(max_length=9)
	grupo = models.CharField(choices=grupos, default=grupos[0], max_length=3)

	class Meta:
		ordering = ["nombres"]
		verbose_name_plural = "Lectores"
		verbose_name = "Lector"

	def __str__(self):
		return "{} - {}".format(self.nombres, self.apellidos)

class Autor(models.Model):
	id_autor = models.CharField(primary_key=True, max_length=8)
	nombres = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)
	email = models.EmailField()
	foto = models.ImageField(upload_to='imagenes/autor', blank=True, null=True)

	class Meta:
		ordering = ["nombres"]
		verbose_name_plural = "Autores"
		verbose_name = "Autor"

	def __str__(self):
		return "{} - {}".format(self.nombres, self.apellidos)

class Pais(models.Model):
	id_pais = models.CharField(primary_key=True, max_length=2)
	nombre = models.CharField(unique=True, max_length=50)

	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "Paises"
		verbose_name = "País"

	def __str__(self):
		return self.nombre

class Editorial(models.Model):
	id_editorial = models.CharField(primary_key=True, max_length=10)
	nombre = models.CharField(max_length=50)
	id_pais = models.ForeignKey(
		Pais,
		on_delete=models.CASCADE,
		verbose_name="País"
	)
	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "Editoriales"
		verbose_name = "Editorial"

	def __str__(self):
		return self.nombre

class Libro(models.Model):
	id_libro = models.CharField(primary_key=True, max_length=12)
	titulo = models.CharField(max_length=200)
	anio = models.IntegerField(default=2000)
	paginas = models.IntegerField()
	foto = models.ImageField(upload_to='imagenes/libro', blank=True, null=True)
	contenido = models.FileField(upload_to='archivos/contenido', blank=True, null=True)
	id_editorial = models.ForeignKey(
		Editorial,
		on_delete=models.CASCADE,
		verbose_name="Editorial"
	)
	ids_autor = models.ManyToManyField(
		Autor,
		verbose_name="Autores"
	)

	class Meta:
		ordering = ["titulo"]
		verbose_name_plural = "Libros"
		verbose_name = "Libro"

	def __str__(self):
		return self.titulo

class Prestamo(models.Model):
	id = models.AutoField(primary_key=True)
	fecha_entrada = models.DateField(auto_now=True)
	hora_entrada = models.TimeField(auto_now=True)
	fecha_salida = models.DateField(auto_now=True)
	hora_salida = models.TimeField(auto_now=True)
	id_libro = models.OneToOneField(
		Libro,
		on_delete=models.CASCADE,
		verbose_name="Libro"
	)
	id_lector = models.ForeignKey(
		Lector,
		on_delete=models.CASCADE,
		verbose_name="Lector"
	)

	class Meta:
		ordering = ["fecha_salida", "hora_entrada"]
		verbose_name_plural = "Prestamos"
		verbose_name = "Prestamo"

	def __str__(self):
		return "{} - {} {}".format(self.id_libro.titulo, self.id_lector.nombres, self.id_lector.apellidos)