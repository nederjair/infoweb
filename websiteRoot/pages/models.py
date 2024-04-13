from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12, unique=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    height = models.IntegerField('image height',default=100)
    width = models.IntegerField('image width',default=100)
    update_date = models.DateTimeField('Last_Updated')
    bodytext = models.TextField('Page Content', blank=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='contacts/%Y/%m/%d', blank=True)
    height = models.IntegerField('image height',default=100)
    width = models.IntegerField('image width',default=100)
    charge = models.CharField('charge', max_length=60)
    departament = models.CharField('departament', max_length=60)
    description = models.TextField('about yourself', blank=True)

    def __str__(self):
        return self.name
