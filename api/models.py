from django.db import models


# contact modeli
class Contact(models.Model):
    fullname = models.CharField(max_length=200) # FISH
    phone = models.CharField(max_length=20) # telefon raqami
    direction = models.CharField(max_length=50) # yunalish

    def __str__(self):
        return self.fullname
    
