from django.db import models

# Create your models here.
# This class(model) will be added to the admin site and will be a form on the website to input data
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=60, default="", blank=True, null=False)
    campus_id = models.IntegerField(default="", blank=True, null=False)
    
    
    def __str__(self):
        display_campus = '{0.campus_name}: {0.state}'
        return display_campus.format(self)
    
    class Meta:
        verbose_name_plural = "University Campus"