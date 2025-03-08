from django.db import models
class Autor(models.Model):
    id_autor=models.AutoField(primary_key=True,editable=False,db_column='T001IdAutor')
    nombre_Autor=models.CharField(max_length=100, db_column='T001NombreAutor')
    apellido_Autor=models.CharField(max_length=100,db_column='T001ApellidoAutor')
    biografia_Autor=models.CharField(max_length=1000,db_column='T001BiografiaAutor')
    def __str__(self):
        return f"{self.nombre_Autor}{self.apellido_Autor}"
    class Meta:
        db_table='T001Autor'
        verbose_name='Autor'
        verbose_name_plural='Autores'
class Editorial (models.Model):
    id_Editorial=models.AutoField(primary_key=True, editable=False,db_column='T002IdEditorial')
    nombre_Editorial=models.CharField(max_length=100,db_column='TOO2NombreEditorial')
    direccion_Editorial=models.CharField(max_length=100,db_column='T002DirecionEditorial')
    telefono_Editorial=models.CharField(max_length=20,db_column='T002TelefonoEditorial')
    def __str__(self):
        return f"{self.nombre_Editorial}"
    class Meta:
        db_table='T002Editorial'
        verbose_name='Editorial'
        verbose_name_plural='Editoriales'

class Libro (models.Model):
    id_libro=models.AutoField(primary_key=True,editable=False,db_column='T003IdLibro')
    titulo_libro=models.CharField(max_length=100,db_column='T003TituloLibro')
    resumen_libro=models.CharField(max_length=100,db_column='T003ResumenLibro')
    ISBN_libro=models.CharField(max_length=40,db_column='T003ISBNLibro')
    aniopublicacion_libro=models.DateField(db_column='T003AñoPublicacion')
    autor=models.ForeignKey(Autor,on_delete=models.CASCADE,related_name='libros',db_column='T003IdAutor')
    editorial=models.ForeignKey(Editorial,on_delete=models.CASCADE,related_name='libros',db_column='T003IdEditorial')

    def __str__(self):
        return self.id_libro
    class Meta:
        db_table='T003Libro'
        verbose_name='Libro'
        verbose_name_plural='Libros'

class Miembro(models.Model):
    Id_miembro=models.AutoField(primary_key=True,editable=False,db_column='T004IdMiembro')
    nombre_miembro=models.CharField(max_length=100,db_column='T004NombreMiembro')
    apellido_miembro=models.CharField(max_length=100,db_column='T004ApellidoMiembro')
    email_Mienbro=models.CharField(unique=True,db_column='T004Email')
    fechamembresia=models.DateField(db_column="T004FechaMembresia")

    def __str__(self):
        return f"{self.nombre_miembro}"
    class Meta:
        db_table='T004Miembro'
        verbose_name='Miembro'
        verbose_name_plural='Miembros'

class Prestamo(models.Model):
    Id_prestamo=models.AutoField(primary_key=True,editable=False,db_column="T005IdPrestamo")
    fecha_prestamo=models.DateField(db_column='T005FechaPrestamo')
    fecha_devolucion=models.DateField(null=True,blank=True,db_column='T006FechaDevolucion')
    libro=models.ForeignKey(Libro,on_delete=models.CASCADE,related_name='libros',db_column='T005IdLibros')
    miembro=models.ForeignKey(Miembro,on_delete=models.CASCADE,related_name='mienbros',db_column='T005IdMiembro')
    def __str__(self):
        return self.Id_prestamo
    class Meta:
        db_table='T005Prestamo'
        verbose_name='Prestamo'
        verbose_name_plural='Prestamo'

