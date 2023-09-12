from django.db import models

# Create your models here.
class contact(models.Model):
    name= models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    email= models.EmailField(max_length=122)
    enquiry = models.CharField(max_length=222)
    date =models.DateField()
    def __str__(self):
        return self.name