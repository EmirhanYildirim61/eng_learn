from django.db import models

# Create your models here.
class Word(models.Model):
    english = models.CharField(max_length=255)
    turkish = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.english} - {self.turkish}"