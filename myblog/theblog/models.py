from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    titulo_tag = models.CharField(max_length=255, default="")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    articulo = models.TextField()

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)

    def get_absolute_url(self):
        #return reverse('detalle_articulo', args=(str(self.id)))
        return reverse('home')
