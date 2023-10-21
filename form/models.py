from django.db import models

# Create your models here.
from django.db import models

class Contact(models.Model):#contact-us 
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name

class Register(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    degree=models.CharField(max_length=30, null=True)
    phone=models.CharField(max_length=15)
    branch=models.CharField(max_length=20)
    topic=models.CharField(max_length=50)
    query=models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class updates(models.Model):
    email=models.EmailField(max_length=25)
    
    def __str__(self):
        return self.email

class Branches(models.Model):
    name=models.CharField(max_length=25)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/", null=True)
    image2 = models.ImageField(upload_to="media/", null=True) 
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE)
    description = models.TextField()
    components = models.TextField(max_length=255, null=True)
    application_area = models.TextField(null=True)
    
    def __str__(self):
        return self.title