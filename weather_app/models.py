from django.db import models

# Create your models here.


class City(models.Model):

    city_name = models.CharField(max_length=35)

    class Meta:
        # verbose_name_ = 'Cities'
        verbose_name_plural = 'City'
        # ordering = ['city_name']

    def __str__(self):
        return self.city_name