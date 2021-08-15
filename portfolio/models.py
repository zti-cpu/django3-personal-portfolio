from django.db import models


# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')  # ImageField = где хранится файл фото
    url = models.URLField(blank=True)#blank=True открытие в новой ссылке

    def __str__(self):
        return self.title