from django.db import models

class Conica(models.Model):
    tipo = models.CharField(max_length=50)
    ecuacion = models.TextField()
    propiedades = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

class Historial(models.Model):
    tipo = models.CharField(max_length=50)
    unidad = models.CharField(max_length=100, blank=True, null=True)
    problema = models.TextField()
    respuesta = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

class Archivo(models.Model):
    nombre = models.CharField(max_length=200)
    archivo = models.FileField(upload_to="uploads/")
    fecha = models.DateTimeField(auto_now_add=True)

class Unit(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='questions')
    problem = models.TextField()
    answer = models.CharField(max_length=500)
    explanation = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.problem[:50]

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text