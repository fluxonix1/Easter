from django.db import models

class Contact_Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return f'Message from {self.name}'

# Create your models here.
