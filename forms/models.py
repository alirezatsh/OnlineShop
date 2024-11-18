from django.db import models

class AboutUs(models.Model):
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=11)
    comment = models.TextField()
    
    def __str__(self):
        return f'{self.name}-{self.lastName}'
    
    
class Installment(models.Model):
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=11)
    productName = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.name}-{self.lastName}'