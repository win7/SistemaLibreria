from django.urls import path
from Datos import views

urlpatterns = [
	path("", views.inicio, name="inicio"),

	path("crear_lector/", views.crear_lector, name="crear_lector"),
	path("listar_lector/", views.listar_lector, name="listar_lector"),
	path("obtener_lector/<str:id>", views.obtener_lector, name="obtener_lector"),
	path("actualizar_lector/", views.actualizar_lector, name="actualizar_lector"),
	path("eliminar_lector/<str:id>", views.eliminar_lector, name="eliminar_lector"),

	path("crear_autor/", views.crear_autor, name="crear_autor"),
	path("listar_autor/", views.listar_autor, name="listar_autor"),
	path("obtener_autor/<str:id>", views.obtener_autor, name="obtener_autor"),
	path("actualizar_autor/", views.actualizar_autor, name="actualizar_autor"),
	path("eliminar_autor/<str:id>", views.eliminar_autor, name="eliminar_autor"),

	path("crear_editorial/", views.crear_editorial, name="crear_editorial"),
	path("listar_editorial/", views.listar_editorial, name="listar_editorial"),
	path("obtener_editorial/<str:id>", views.obtener_editorial, name="obtener_editorial"),
	path("actualizar_editorial/", views.actualizar_editorial, name="actualizar_editorial"),
	path("eliminar_editorial/<str:id>", views.eliminar_editorial, name="eliminar_editorial"),

	path("crear_libro/", views.crear_libro, name="crear_libro"),
	path("listar_libro/", views.listar_libro, name="listar_libro"),
	path("obtener_libro/<str:id>", views.obtener_libro, name="obtener_libro"),
	path("actualizar_libro/", views.actualizar_libro, name="actualizar_libro"),
	path("eliminar_libro/<str:id>", views.eliminar_libro, name="eliminar_libro"),
]