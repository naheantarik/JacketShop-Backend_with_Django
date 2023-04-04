from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    price = models.IntegerField(null=True)
    image = models.ImageField(default='profile1.jpg', upload_to='Media/product')
    descriptions = models.CharField(max_length=100,default='', null=True, blank=True)

    @staticmethod
    def all_product():
        return Product.objects.all()
    
    def __str__(self):
        return self.name
