from django.db import models

# Create your models here.
class Contact(models.Model):

    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    created = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=750)
    subject = models.CharField(max_length=255)
    def __str__(self):
        return self.subject