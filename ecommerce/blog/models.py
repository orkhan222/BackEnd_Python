from django.db import models

from django.db.models.fields.related import ForeignKey

# Create your models here.

class Post(models.Model):
    name= models.CharField(max_length=127,null=True,blank=True)
    text = models.CharField(max_length=127,null=True,blank=True)
    image = models.ImageField(null=True,blank=True)


    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'



    def __str__(self):
        return self.name

    
class Commet(models.Model):
    name= models.TextField(max_length=127,null=True,blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='commets')

    class Meta:
        verbose_name='Commet'
        verbose_name_plural='Commets'


    def __str__(self):
        return self.name



