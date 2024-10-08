from django.db import models

# Create your models here.

class Book(models.Model): 
    title = models.CharField(max_length=100,null=False, blank=False)
    author = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    published_date = models.DateField(null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title