from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.title
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField(Course, related_name='students') #esta linea muestra la relacion entre estudiants y el curso
    
    def __str__(self):
        return self.name
