from django.db import models
from django.contrib.auth.models import User #needed for OneToOneField

# Create your models here.


class SalesPerson(models.Model):
    username= models.OneToOneField(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=120)
    bio= models.TextField(default='No bio...')
    pic = models.ImageField(upload_to='customers', default='no_picture.jpg')

    def __str__(self):
        return f"Profile of {self.user.username}"
        