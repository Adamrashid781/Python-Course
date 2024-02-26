from django.db import models

# Create your models here.
TYPE_CHOICES = (
    ('appetizers', 'appetizers'),
    ('entrees', 'entrees'),
    ('treats', 'treats'),
    ('drinks', 'drinks'),
    
)   



class Product (models.Model):
    type = models.CharField( max_length=50, choices = TYPE_CHOICES) # Blank is for the forms, null is for the database
    name = models.CharField( max_length=50, default = '', blank = True, null=False)
    description = models.TextField(max_length = 300, default ='', blank = True)
    # DecimalField must have a 'max_digits', and a 'decimal_places'
    price = models.DecimalField( default = 0.00, max_digits=10000, decimal_places=2)
    image = models.CharField( max_length=255, default ='', blank = True)

    objects = models.Manager()
    
    def __str__(self):
        return self.name