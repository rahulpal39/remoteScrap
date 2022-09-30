
from django.db import models

# Create your models here.


class Jobs(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(unique=True)     
    image=models.ImageField()
    applylink=models.URLField()


    def __str__(self):
        return self.title
