from django.db import models


# Create your models here.
class user(models.Model):
    fname=models.CharField(max_length=50)
    email=models.CharField(max_length=50,unique=True)
    mobile=models.CharField(max_length=20)
    address=models.TextField()
    password=models.CharField(max_length=50)
     
    def __str__(self):
        return self.fname

class Emergency_Contact(models.Model):

    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    occupation=models.CharField(max_length=50)


    def __str__(self):
        return self.name+' '+self.occupation



class Event_gallery(models.Model):
    name= models.CharField(max_length=50)
    date=models.DateField()
    disc=models.CharField(max_length=50)
    pics=models.FileField(upload_to='profile',null=True,blank=True)
    def __str__(self):
        return self.name

class Society_members_information_management(models.Model):
    flatno=models.CharField(max_length=50)
    member= models.CharField(max_length=50)
    numberofmember=models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    
    def __str__(self):
        return self.flatno


        
class Notifications(models.Model):
    name= models.CharField(max_length=50)
    date=models.DateField()
    disc=models.TextField(max_length=150)
    def __str__(self):
        return self.name


   
    
    
    

    



