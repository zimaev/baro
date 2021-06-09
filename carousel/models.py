from django.db import models


class Carousel(models.Model):
    
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='images/carusel', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name