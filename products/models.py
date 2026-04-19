from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    points_required = models.IntegerField()
    stock = models.IntegerField(default=10)