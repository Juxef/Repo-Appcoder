from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from appcoder.models import Curso, Profesor, Estudiante
from django.template import loader

# Create your views here.
"""
def agregar(request, nom, ed, fecha):
    familiar = Familiar(nombre=nom, edad = ed, fechanac = fecha)
    familiar.save()
    texto = f"Se guardo en la BD el familiar: {familiar.nombre}, edad: {familiar.edad}, Fecha de nac: {familiar.fechanac}"
    return HttpResponse(texto)
"""
def curso(request):

      curso =  Curso(nombre="Desarrollo web", camada="1981")
      curso.save()
      curso =  Curso(nombre="Matemática", camada="3217")
      curso.save()
      curso =  Curso(nombre="Física", camada="8925")
      curso.save()
      curso =  Curso(nombre="Química", camada="1132")
      curso.save()
      documentoDeTexto = f"Curso: {curso.nombre}   Camada: {curso.camada}"
      return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "inicio.html")

def cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos":cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def profesores(request):

      prof = Profesor.objects.all()
      dicc = {"profesores":prof}
      plantilla = loader.get_template("profesores.html")
      documento = plantilla.render(dicc)
      return HttpResponse(documento)
 

def estudiantes(request):

      est = Estudiante.objects.all()
      dicc = {"estudiantes":est}
      plantilla = loader.get_template("estudiantes.html")
      documento = plantilla.render(dicc)
      return HttpResponse(documento)