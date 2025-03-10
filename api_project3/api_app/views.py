from django.shortcuts import get_object_or_404  # Importa una función para obtener un objeto o devolver un error 404 si no se encuentra
from rest_framework.response import Response  # Importa la clase Response para devolver respuestas HTTP
from rest_framework import generics, status  # Importa clases genéricas y códigos de estado HTTP
from rest_framework.exceptions import NotFound, ValidationError  # Importa excepciones para manejar errores específicos
from .models import Libro, Autor, Editorial, Miembro, Prestamo
from .serializers import LibroSerializer, AutorSerializer, EditorialSerializer, MiembroSerializer, PrestamoSerializer

# Create your views here.


#---------------CRUD Autor-------------------
class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()  # Define el conjunto de consultas para obtener todas las personas
    serializer_class = AutorSerializer  # Define el serializador a utilizar

    # Método GET para listar todas las personas
    def get(self, request):
        autor = Autor.objects.all()  # Obtiene todas las personas
        serializer = AutorSerializer(autor, many=True)  # Serializa las personas
        if not autor:
            raise NotFound('No se encontraron personas.')  # Lanza una excepción si no se encuentran personas
        return Response({'success': True, 'detail': 'Listado de personas.', 'data': serializer.data}, status=status.HTTP_200_OK)  # Devuelve una respuesta con los datos serializados


from .models import Libro, Autor, Editorial, Miembro, Prestamo
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import LibroSerializer, AutorSerializer, EditorialSerializer, MiembroSerializer, PrestamoSerializer
from rest_framework import generics, filters

# Create your views here.


#---------------CRUD Autor-------------------

#Permite listar y crear registros
class ListCreateAutor(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

#Permite ver, actualizar y eliminar
class RetrieveUpdateDeleteAutor(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

#---------------CRUD Editorial-------------------
class ListCreateEditorial(generics.ListCreateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

class RetrieveUpdateDeleteEditorial(generics.RetrieveUpdateDestroyAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

#---------------CRUD Libro-------------------
class ListCreateLibro(generics.ListCreateAPIView):
    serializer_class = LibroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['autor', 'editorial']  # Permite filtrar por autor y editorial

    def get_queryset(self):
        return Libro.objects.all()

class RetrieveUpdateDeleteLibro(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

#---------------CRUD Miembro-------------------
class ListCreateMiembro(generics.ListCreateAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

class RetrieveUpdateDeleteMiembro(generics.RetrieveUpdateDestroyAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

#---------------CRUD Prestamo-------------------
class ListCreatePrestamo(generics.ListCreateAPIView):
    serializer_class = PrestamoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['fecha_prestamo', 'miembro']  # Filtra por fecha o por miembro

    def get_queryset(self):
        return Prestamo.objects.all()

class RetrieveUpdateDeletePrestamo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer