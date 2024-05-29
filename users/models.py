from django.db import models
from django.conf import settings

# Create your models here.
class Users(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    surname=models.CharField(max_length=150)
    work=models.CharField(max_length=150)
    about=models.TextField()
    create_time=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} {self.surname} | {self.author}"