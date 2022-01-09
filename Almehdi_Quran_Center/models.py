from typing import Counter
from django.db import models

# Create your models here.

class slider(models.Model):
    title=models.CharField(max_length=150)
    tag_line=models.CharField(max_length=250)
    slider_img=models.ImageField(upload_to='static/assets/img/hero-carousel')
    def __str__(self):
        return self.title

class Enroll(models.Model):
    fullname=models.CharField(max_length=150,default="name")
    email=models.EmailField()
    mobile=models.CharField(max_length=15)
    country=models.CharField(max_length=200)
    gender=models.CharField(max_length=10)
    def __str__(self):
        return self.fullname

class Team(models.Model):
    t_name=models.CharField(max_length=150)
    t_role=models.CharField(max_length=250)
    t_fb_username=models.CharField(max_length=50)
    t_twitter_username=models.CharField(max_length=50)
    t_insta_username=models.CharField(max_length=50)
    t_img=models.ImageField(upload_to='static/assets/img/team')
    def __str__(self):
        return self.t_name   


class Tesmonial(models.Model):
    name=models.CharField(max_length=150)
    role=models.CharField(max_length=250)
    msg=models.CharField(max_length=500)
    slider_img=models.ImageField(upload_to='static/assets/img/hero-carousel')
    def __str__(self):
        return self.name


class Contact(models.Model):
    name=models.CharField(max_length=150,default="name")
    email=models.EmailField()
    subject=models.CharField(max_length=150,default="subject")
    msg=models.CharField(max_length=590,default="msg")
    def __str__(self):
        return self.name
