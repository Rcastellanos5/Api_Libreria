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
