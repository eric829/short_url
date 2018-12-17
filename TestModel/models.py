# models.py
from django.db import models
 
class Test(models.Model):
    typein = models.CharField(max_length=20)
    short_name = models.CharField(max_length=256,default='SOME STRING')

    def __str__(self):
    	#return "{0}, {1}".format(self.typein, self.short_name)
        return '%s %s'%(self.typein, self.short_name)