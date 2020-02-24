from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    appreviation = models.CharField(max_length=15)
    country = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    lob = models.CharField(max_length = 30)
    def __str__(self):
        return self.name



class Deal(models.Model):

    name = models.CharField(max_length = 20)
    creation_date =models.DateField()
    date_lastupdated = models.DateField(auto_now=True)
    status = models.CharField(max_length = 20) ##in progress or win or loss
    status_descriptian = models.TextField()
    deal_source = models.CharField(max_length=50)
    third_party = models.CharField(max_length=50)
    project= models.CharField(max_length=50)
    margin_type = models.CharField(max_length=50)
    new_renew = models.CharField(max_length=10)
    sub_perpcual = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    def __str__(self):
        return self.name





### add primary key: id = models.AutoField(primary_key=True)
'''
class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique= True)

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=264,unique= True)
    url = models.URLField(unique=True)
    def __str__(self):
        return self.name


class  AccessRecrd(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.PROTECT)
    date = models.DateField()
    def __str__(self):
        return str(self.date)

'''
