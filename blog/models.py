from django.db import models
from django.utils import timezone

#DEFINIMOS EL MODELO (OBJETO) Y SUS ATRIBUTOS ASÍ COMO MÉTODOS
#models.Model es un modelo de Django
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    #método en el que crea la hora de publicación en el blog
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #método que devuelve el título del post
    def __str__(self):
        return self.title
