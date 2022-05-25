from django.urls import path

from appcoder import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('cursos/', views.cursos, name="Cursos"),
    path('curso/', views.curso, name="Curso"),
    path('profesores/', views.profesores, name="Profesores"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),

]

