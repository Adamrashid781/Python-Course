from django.db import models

PREFIX_CHOICES = (
    ('Mr.', 'Mr.'),
    ('Ms.', 'Ms.'),
    ('Mrs.', 'Mrs.'),
    ('Dr.', 'Dr.'),
)

# Create your models here.
class Profile(models.Model):
    Prefix = models.CharField( max_length=50,  default = '', choices = PREFIX_CHOICES)
    First_Name = models.CharField( max_length=50, default = '', blank = True, null=False)
    Last_Name = models.CharField( max_length=50, default = '', blank = True, null=False)
    Email = models.EmailField(max_length = 50, default = '', blank = True, null = False)
    Username = models.CharField( max_length=50, default = '', blank = True, null=False)

    objects = models.Manager()


    def __str__(self):
        return self.Username 


