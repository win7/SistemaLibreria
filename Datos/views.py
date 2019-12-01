from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import render

from Datos.models import *

# Create your views here.
def inicio(request):
	return render(request, "inicio.html")

def crear_lector(request):
	if request.method == "GET":
		return TemplateResponse(request, "crear_lector.html")

	elif request.method == "POST":
		try:
			id_lector = request.POST["id_lector"]
			nombres = request.POST["nombres"]
			apellidos = request.POST["apellidos"]
			telefono = request.POST["telefono"]
			grupo = request.POST["grupo"]

			lector = Lector(
				id_lector=id_lector,
				nombres=nombres,
				apellidos=apellidos,
				telefono=telefono,
				grupo=grupo
			)
			lector.save()
			return TemplateResponse(request, "crear_lector.html")

		except Exception as e:
			return TemplateResponse(request, "crear_lector.html")

def listar_lector(request):
	if request.method == "GET":
		lectores = Lector.objects.all()
		return TemplateResponse(request, "listar_lector.html", {"lectores": lectores})

def obtener_lector(request, id):
	if request.method == "GET":
		try:
			lector = Lector.objects.get(id_lector=id)
			return TemplateResponse(request, "editar_lector.html", {"lector": lector})
		except  Lector.DoesNotExist:
			return TemplateResponse(request, "editar_lector.html", {"obtener": "error"})
		
def actualizar_lector(request):
	if request.method == "POST":
		try:
			id_lector = request.POST["id_lector"]
			nombres = request.POST["nombres"]
			apellidos = request.POST["apellidos"]
			telefono = request.POST["telefono"]
			grupo = request.POST["grupo"]

			lector = Lector.objects.get(id_lector=id_lector)
			lector.nombres = nombres
			lector.apellidos = apellidos
			lector.telefono = telefono
			lector.grupo = grupo
			lector.save()

			return HttpResponseRedirect("/listar_lector")

		except Exception as e:
			return HttpResponseRedirect("/listar_lector")

def eliminar_lector(request, id):
	if request.method == "GET":
		try:
			lector = Lector.objects.get(id_lector=id)
			lector.delete()
			return HttpResponseRedirect("/listar_lector")
		except  Lector.DoesNotExist:
			return HttpResponseRedirect("/listar_lector")
		

def crear_autor(request):
	if request.method == "GET":
		return TemplateResponse(request, "crear_autor.html")

	elif request.method == "POST":
		try:
			id_autor = request.POST["id_autor"]
			nombres = request.POST["nombres"]
			apellidos = request.POST["apellidos"]
			email = request.POST["email"]

			if "foto" in request.FILES:
				foto = request.FILES["foto"]
			else:
				foto = None

			autor = Autor(
				id_autor=id_autor,
				nombres=nombres,
				apellidos=apellidos,
				email=email,
				foto=foto
			)
			autor.save()
			return TemplateResponse(request, "crear_autor.html")

		except Exception as e:
			return TemplateResponse(request, "crear_autor.html")


def listar_autor(request):
	if request.method == "GET":
		autores = Autor.objects.all()
		return TemplateResponse(request, "listar_autor.html", {"autores": autores})

def obtener_autor(request, id):
	if request.method == "GET":
		try:
			autor = Autor.objects.get(id_autor=id)
			return TemplateResponse(request, "editar_autor.html", {"autor": autor})
		except  Autor.DoesNotExist:
			return TemplateResponse(request, "editar_autor.html", {"obtener": "error"})
		
def actualizar_autor(request):
	if request.method == "POST":
		try:
			id_autor = request.POST["id_autor"]
			nombres = request.POST["nombres"]
			apellidos = request.POST["apellidos"]
			email = request.POST["email"]

			autor = Autor.objects.get(id_autor=id_autor)
			if "foto" in request.FILES:
				foto = request.FILES["foto"]
			else:
				foto = autor.foto

			autor.nombres = nombres
			autor.apellidos = apellidos
			autor.email = email
			autor.foto = foto
			autor.save()

			return HttpResponseRedirect("/listar_autor")

		except Exception as e:
			return HttpResponseRedirect("/listar_autor")

def eliminar_autor(request, id):
	if request.method == "GET":
		try:
			autor = Autor.objects.get(id_autor=id)
			autor.delete()
			return HttpResponseRedirect("/listar_autor")
		except  Autor.DoesNotExist:
			return HttpResponseRedirect("/listar_autor")

def crear_editorial(request):
	if request.method == "GET":
		paises = Pais.objects.all()
		return TemplateResponse(request, "crear_editorial.html", {"paises": paises})

	elif request.method == "POST":
		try:
			id_editorial = request.POST["id_editorial"]
			nombre = request.POST["nombre"]
			id_pais = request.POST["id_pais"]

			pais = Pais.objects.get(id_pais=id_pais)

			editorial = Editorial(
				id_editorial=id_editorial,
				nombre=nombre,
				id_pais=pais
			)
			editorial.save()

			paises = Pais.objects.all()
			return TemplateResponse(request, "crear_editorial.html", {"paises": paises})

		except Exception as e:
			paises = Pais.objects.all()
			return TemplateResponse(request, "crear_editorial.html", {"paises": paises})

def listar_editorial(request):
	if request.method == "GET":
		editoriales = Editorial.objects.all()
		return TemplateResponse(request, "listar_editorial.html", {"editoriales": editoriales})

def obtener_editorial(request, id):
	if request.method == "GET":
		try:
			paises = Pais.objects.all()
			editorial = Editorial.objects.get(id_editorial=id)
			return TemplateResponse(request, "editar_editorial.html", {"editorial": editorial, "paises": paises})
		except  Editorial.DoesNotExist:
			return TemplateResponse(request, "editar_editorial.html", {"obtener": "error"})

def actualizar_editorial(request):
	if request.method == "POST":
		try:
			id_editorial = request.POST["id_editorial"]
			nombre = request.POST["nombre"]
			id_pais = request.POST["id_pais"]

			pais = Pais.objects.get(id_pais=id_pais)

			editorial = Editorial.objects.get(id_editorial=id_editorial)
			editorial.nombre = nombre
			editorial.id_pais = pais
			editorial.save()

			return HttpResponseRedirect("/listar_editorial")

		except Exception as e:
			return HttpResponseRedirect("/listar_editorial")

def eliminar_editorial(request, id):
	if request.method == "GET":
		try:
			editorial = Editorial.objects.get(id_editorial=id)
			editorial.delete()
			return HttpResponseRedirect("/listar_editorial")
		except  Editorial.DoesNotExist:
			return HttpResponseRedirect("/listar_editorial")

def crear_libro(request):
	if request.method == "GET":
		editoriales = Editorial.objects.all()
		autores = Autor.objects.all()

		return TemplateResponse(request, "crear_libro.html",{"editoriales": editoriales, "autores": autores})

	elif request.method == "POST":
		try:
			id_libro = request.POST["id_libro"]
			titulo = request.POST["titulo"]
			anio = request.POST["anio"]
			paginas = request.POST["paginas"]
			id_editorial = request.POST["id_editorial"]
			ids_autor = request.POST.getlist("ids_autor")

			if "foto" in request.FILES:
				foto = request.FILES["foto"]
			else:
				foto = None

			if "contenido" in request.FILES:
				contenido = request.FILES["contenido"]
			else:
				contenido = None

			editorial = Editorial.objects.get(id_editorial=id_editorial)
			
			libro = Libro(
				id_libro=id_libro,
				titulo=titulo,
				anio=anio,
				paginas=paginas,
				foto=foto,
				contenido=contenido,
				id_editorial=editorial
			)
			libro.save()
			
			for item in ids_autor:
				autor = Autor.objects.get(id_autor=item)
				libro.ids_autor.add(autor)

			editoriales = Editorial.objects.all()
			autores = Autor.objects.all()

			return TemplateResponse(request, "crear_libro.html",{"editoriales": editoriales, "autores": autores})

		except Exception as e:
			editoriales = Editorial.objects.all()
			autores = Autor.objects.all()

			return TemplateResponse(request, "crear_libro.html",{"editoriales": editoriales, "autores": autores})

def listar_libro(request):
	if request.method == "GET":
		libros = Libro.objects.all()
		return TemplateResponse(request, "listar_libro.html", {"libros": libros})

def obtener_libro(request, id):
	if request.method == "GET":
		try:
			libro = Libro.objects.get(id_libro=id)
			editoriales = Editorial.objects.all()
			autores = Autor.objects.all()
			return TemplateResponse(request, "editar_libro.html", {"libro": libro,"editoriales": editoriales, "autores": autores})
		except  Libro.DoesNotExist:
			editoriales = Editorial.objects.all()
			autores = Autor.objects.all()
			return TemplateResponse(request, "editar_libro.html", {"obtener": "error", "editoriales": editoriales, "autores": autores})

def actualizar_libro(request):
	if request.method == "POST":
		try:
			id_libro = request.POST["id_libro"]
			titulo = request.POST["titulo"]
			anio = request.POST["anio"]
			paginas = request.POST["paginas"]
			id_editorial = request.POST["id_editorial"]
			ids_autor = request.POST.getlist("ids_autor")

			libro = Libro.objects.get(id_libro=id_libro)
			if "foto" in request.FILES:
				foto = request.FILES["foto"]
			else:
				foto = libro.foto

			if "contenido" in request.FILES:
				contenido = request.FILES["contenido"]
			else:
				contenido = libro.contenido

			editorial = Editorial.objects.get(id_editorial=id_editorial)
			
			libro.id_libro = id_libro
			libro.titulo = titulo
			libro.anio = anio
			libro.paginas = paginas
			libro.foto = foto
			libro.contenido = contenido
			libro.id_editorial = editorial
			libro.save()

			for autor in libro.ids_autor.all():
				libro.ids_autor.remove(autor)

			for id_autor in ids_autor:
				autor = Autor.objects.get(id_autor=id_autor)
				libro.ids_autor.add(autor)

			return HttpResponseRedirect("/listar_libro")

		except Exception as e:
			print("Error: {}".format(e))
			return HttpResponseRedirect("/listar_libro")

def eliminar_libro(request, id):
	if request.method == "GET":
		try:
			libro = Libro.objects.get(id_libro=id)
			libro.delete()
			return HttpResponseRedirect("/listar_libro")
		except  Libro.DoesNotExist:
			return HttpResponseRedirect("/listar_libro")


"""
HTTP_200_OK
HTTP_201_CREATED
HTTP_204_NO_CONTENT
HTTP_400_BAD_REQUEST
HTTP_401_UNAUTHORIZED
HTTP_403_FORBIDDEN """