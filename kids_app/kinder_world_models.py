from django.db import models

class Parent(models.Model):
    name = models.CharField(max_length=30,default="")
    email = models.EmailField(max_length=50,default="", primary_key=True)
    password = models.CharField(max_length=30,default="")
    phone = models.CharField(max_length=15,default="")
    pic = models.ImageField(upload_to='pic/', default="")
    def __str__(self): #it is used to represent object in string form
        return (self.name)

class Content(models.Model):
    title = models.CharField(max_length=255)
    
    content_type = models.CharField(max_length=100)
    content_file = models.FileField(upload_to='content/')
    def __str__(self): #it is used to represent object in string form
        return (self.title)
       

class Notification(models.Model):
    title = models.CharField(max_length=255)  
    message = models.TextField() 
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self): #it is used to represent object in string form
        return (self.title)
       

class Feedback(models.Model):
    name = models.CharField(max_length=255)  
    email = models.EmailField()  
    rating = models.CharField(max_length=6,default="")
    review = models.TextField()  
    date = models.DateTimeField(auto_now_add=True)
    pic=models.CharField(max_length=100,default="")
    def __str__(self): #it is used to represent object in string form
        return (self.name)
       


class Contact(models.Model):
    name = models.CharField(max_length=255) 
    email = models.EmailField() 
    phone = models.CharField(max_length=13,default="") 
    question = models.TextField()  
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self): #it is used to represent object in string form
        return (self.name)
       
