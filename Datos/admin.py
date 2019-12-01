from django.contrib import admin
from django.utils.html import format_html

from Datos.models import *

# Register your models here.
@admin.register(Lector)
class LectorAdmin(admin.ModelAdmin):
    list_display = ("id_lector", "nombres", "apellidos", "telefono", "grupo")
    list_display_links = ("id_lector", "nombres")
    search_fields = ["nombres", "apellidos", "telefono"]

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("id_autor", "nombres", "apellidos", "email", "get_foto")
    list_display_links = ("id_autor", "nombres")
    search_fields = ["nombres", "apellidos", "email"]

    def get_foto(self, instance):
        try:
            url = instance.foto.url
        except Exception as e:
            url = ""
        return format_html("<img src = '{}'' height='60' width='50' border-radius='2px' alt='Sin Foto'>".format(url))
    get_foto.allow_tags = True
    get_foto.short_description = "Foto"

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ("id_pais", "nombre")
    search_fields = ["nombre"]

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ("id_editorial", "nombre", "id_pais")
    search_fields = ["nombre", "id_pais__nomnre"]

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("id_libro", "titulo", "anio", "paginas", "foto", "contenido",
                    "id_editorial", "mostrar_autores")
    list_display_links = ("id_libro", "titulo")
    search_fields = ["titulo", "anio", "paginas", "foto", "contenido", "id_editorial__nombre",
                     "ids_autor__nombres", "ids_autor__apellidos"]
    raw_id_fields = ("id_editorial",)
    filter_horizontal = ("ids_autor",)

    def mostrar_autores(self, autor):
        return ",".join([str(p) for p in autor.ids_autor.all()])

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ("id", "fecha_entrada", "hora_entrada", "fecha_salida", "hora_salida",
                    "id_libro", "id_lector")
    search_fields = ["fecha_entrada", "hora_entrada", "fecha_salida", "hora_salida",
                     "id_libro__titulo", "id_lector__nombres", "id_lector__apellidos"]
    raw_id_fields = ("id_libro", "id_lector")