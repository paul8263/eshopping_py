from django.db import models

# Create your models here.


class Commodity(models.Model):
    name = models.CharField(blank=False, null=False, max_length=512)
    description = models.CharField(blank=False, null=False, max_length=5000)
    price = models.DecimalField(max_digits=8, decimal_places=2)


class CommodityImage(models.Model):
    commodity = models.ForeignKey('Commodity', on_delete=models.CASCADE)
    image = models.ImageField()
