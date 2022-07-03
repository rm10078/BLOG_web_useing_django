from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField        #for text editor
from autoslug import AutoSlugField                  #for auto slug

# Create your models here.
class blogpost(models.Model):                           #Model / database for blogpost
    title=models.CharField(max_length=30)
    des=models.TextField(max_length=1000)
    bdes=models.TextField(max_length=3000)
    content=FroalaField()
    slug=AutoSlugField(populate_from='title',unique=True,null=True,default=None)
    image=models.ImageField(upload_to='images')
    created_at=models.DateTimeField(auto_now_add=True)
    upload_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Contact(models.Model):                              #model/database for contact form
    uname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=20)
    desc=models.TextField(max_length=8000)
    date=models.DateField()

    def __str__(self):  
        return self.uname
    

class Event(models.Model):
    ev_title=models.CharField(max_length=50)
    ev_des=models.TextField(max_length=3000)
    ev_slug=AutoSlugField(populate_from='ev_title',unique=True,null=True,default=None)
    ev_content=FroalaField()
    ev_img=models.ImageField(upload_to='ev_images')

    def __str__(self):
        return self.ev_title

class News(models.Model):
    n_title=models.CharField(max_length=50)
    n_des=models.TextField(max_length=3000)
    n_slug=AutoSlugField(populate_from='n_title',unique=True,null=True,default=None)
    n_content=FroalaField()
    n_img=models.ImageField(upload_to='news_images')

    def __str__(self):
        return self.n_title
