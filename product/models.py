from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    description = models.TextField(default="")
    image = models.ImageField(upload_to="products/")
    
    class Meta:
        db_table = "products"



# Client-> Data => Receive (Serialization Process, convert to py)-> Business Logc -> Send Some Data In Python (Deserialization to raw) 