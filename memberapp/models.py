from django.db import models
# Create your models here.

class Complain(models.Model):
    name=models.CharField(max_length=50)
    flat=models.CharField(max_length=50)
    mobile=models.CharField(max_length=20)
    description=models.CharField(max_length=50)
     
    def __str__(self):
        return self.name


class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,unique=True)
    mobile=models.CharField(max_length=20)
    address=models.TextField()
    password=models.CharField(max_length=50)
     
    def __str__(self):
        return self.name

class Pay(models.Model):
    uid= models.ForeignKey(User,on_delete=models.CASCADE)
    paydate=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

