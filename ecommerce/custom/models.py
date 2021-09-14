from django.db import models

# Create your models here.
class Custom(models.Model):
    user= models.CharField(max_length=127,null=True,blank=True)
    number = models.CharField(max_length=127,null=True,blank=True)

    class Meta:
        verbose_name='Custom'
        verbose_name_plural='Customs'


    def __str__(self):
        return self.user