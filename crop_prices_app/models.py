# homepage/models.py
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Crop(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Price(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

