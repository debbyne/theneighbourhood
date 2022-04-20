import email
from django.db import models
from django.contrib.auth.models import User
from unicodedata import name
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
import datetime as dt
# Create your models here.
class Neighbourhood(models.Model):
    name=models.CharField(max_length=50, blank=True)
    location =models.CharField(max_length=50, blank=True)
    image = CloudinaryField('image')
    description = models.TextField(max_length=1000, null=True)
    occupants_count = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def _str_(self):
        return self.name
    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def find_neighbourhood(cls, id):
        return cls.objects.filter(id=id)
    @classmethod
    def update_neighbourhood(cls, id ,name):
        return cls.objects.filter(id=id).update()


class Profile(models.Model):
     name=models.CharField(max_length=50, blank=True)
     email=models.EmailField(max_length=50, blank=True)
     user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="Profile",null=True)
     location =models.CharField(max_length=50, blank=True)
     neighbourhood_name =  models.CharField(max_length=50, blank=True)
     house=models.CharField(max_length=50, blank=True)
     def __str__(self):
        return self.name

     @receiver(post_save, sender=User)
     def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

     @receiver(post_save, sender=User)
     def save_user_profile(sender, instance, **kwargs):
        instance.save()

     def save_profile(self):
        self.user

     def delete_profile(self):
        self.delete()

     def __str__(self):
        return self.user.username


     @classmethod
     def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

     def __str__(self):
        return f'{self.user.username} Profile'

class Post(models.Model):
    title=models.CharField(max_length=30, blank=True)
    post = models.TextField()
    date= models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="owner")
    hood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,related_name="post")

    def __str__(self):
        return self.title

    @classmethod
    def search_project_name(cls, search_term):
        return cls.objects.filter(
        title__icontains=search_term)
        

class Business(models.Model):
     name=models.CharField(max_length=50, blank=True)
     user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='owner')   
     location =models.CharField(max_length=50, blank=True)
     contact = models.IntegerField(default=0, blank=True)
     image = CloudinaryField('image')
     neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.SET_NULL, null=True,related_name='business',blank=True)
     email=models.EmailField(max_length=50, blank=True)


     def __str__(self):
        return f'{self.user.username} Business'

     def create_business(self):
        self.save()

     def delete_business(self):
        self.delete()



