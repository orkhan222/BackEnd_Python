from django.db import models

from django.db.models.fields.related import ForeignKey

# Create your models here.

class Post(models.Model):
    title= models.CharField(max_length=127,null=True,blank=True)
    text = models.CharField(max_length=127,null=True,blank=True)
    image = models.ImageField(null=True,blank=True)


    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'



    def __str__(self):
        return self.title

    
class Commet(models.Model):
    title= models.CharField(max_length=127,null=True,blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')

    class Meta:
        verbose_name='Commet'
        verbose_name_plural='Commets'


    def __str__(self):
        return self.title
