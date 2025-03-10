from django.urls import path

from .views import (
    ListCreateAutor, RetrieveUpdateDeleteAutor,
    ListCreateEditorial, RetrieveUpdateDeleteEditorial,
    ListCreateLibro, RetrieveUpdateDeleteLibro,
    ListCreateMiembro, RetrieveUpdateDeleteMiembro,
    ListCreatePrestamo, RetrieveUpdateDeletePrestamo
)

urlpatterns = [
    # Rutas para Autor
    path('api/autores/', ListCreateAutor.as_view(), name='listar_crear_autor'),
    path('api/autores/<int:pk>/', RetrieveUpdateDeleteAutor.as_view(), name='detalle_autor'),

    # Rutas para Editorial
    path('api/editoriales/', ListCreateEditorial.as_view(), name='listar_crear_editorial'),
    path('api/editoriales/<int:pk>/', RetrieveUpdateDeleteEditorial.as_view(), name='detalle_editorial'),

    # Rutas para Libro
    path('api/libros/', ListCreateLibro.as_view(), name='listar_crear_libro'),
    path('api/libros/<int:pk>/', RetrieveUpdateDeleteLibro.as_view(), name='detalle_libro'),

    # Rutas para Miembro
    path('api/miembros/', ListCreateMiembro.as_view(), name='listar_crear_miembro'),
    path('api/miembros/<int:pk>/', RetrieveUpdateDeleteMiembro.as_view(), name='detalle_miembro'),

    # Rutas para Prestamo
    path('api/prestamos/', ListCreatePrestamo.as_view(), name='listar_crear_prestamo'),
    path('api/prestamos/<int:pk>/', RetrieveUpdateDeletePrestamo.as_view(), name='detalle_prestamo'),
]
