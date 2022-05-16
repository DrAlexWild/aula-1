from django.db import models

# Create your models here.

#autor data titulo descricao

class Blog_Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    data = models.DateField()
    descricao = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.titulo[:50]

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    prioridade = models.IntegerField(default=1)
    concluido = models.BooleanField(default=False)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo[:50]
