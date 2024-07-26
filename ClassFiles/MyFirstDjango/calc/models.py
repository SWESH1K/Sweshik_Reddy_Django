from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=300, null=True)
    age = models.CharField(max_length=300, null=True)
    date = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):

    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor')
    )

    name = models.CharField(max_length=300, null=True)
    price = models.CharField(max_length=300, null=True)
    category = models.CharField(max_length=300, choices=CATEGORY)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name