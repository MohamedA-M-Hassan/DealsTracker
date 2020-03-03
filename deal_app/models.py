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


## Customer - Ejada info - Summary file: EjadacColumns=e_ , CustomerColumns= c_, generaLColumns= g_
class Deal(models.Model):

    ## general columns
    name = models.CharField(max_length = 20)
    ## one to many relation
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)

    creation_date =models.DateField()
    date_lastupdated = models.DateField(auto_now=True)
    status = models.CharField(max_length = 20) ##in progress or win or loss

    ## Ejada columns to be used in summary file
    status_descriptian = models.TextField()
    deal_source = models.CharField(max_length=50)
    third_party = models.CharField(max_length=50)
    project= models.CharField(max_length=50)
    margin_type = models.CharField(max_length=50)
    new_renew = models.CharField(max_length=10)
    sub_perpcual = models.CharField(max_length=50)



    ## Customer fields to be added by himself


    def __str__(self):
        return self.name


class Deal_Items_Price_Lookup(models.Model):
    creator_on_prem_price_per_month_dollar = 70
    creator_on_prem_price_per_month_dollar = 0
    explorer_on_prem_price_per_month_dollar = 0
    viewer_on_prem_price_per_month_dollar = 0
    term_desktop_personal_price_per_month_dollar = 0
    term_desktop_professional_price_per_month_dollar = 0
    term_server_core_price_per_month_dollar = 0
    term_server_interactor_price_per_month_dollar = 0
    tableau_online_price_per_month_dollar = 0
    server_management_price_per_month_dollar = 0
    creator_online_price_per_month_dollar = 0
    explorer_online_price_per_month_dollar = 0
    viewer_online_price_per_month_dollar = 0
    perpetual_desktop_personal_price_per_month_dollar = 0
    perpetual_desktop_professinal_price_per_month_dollar = 0
    perpetual_server_core_price_per_month_dollar = 0
    perpetual_server_interactor_price_per_month_dollar = 0
    data_management_online_price_per_month_dollar = 0
    data_management_on_premise_price_per_month_dollar = 0
    def __str__(self):
        return self.name

class Deal_Items(models.Model):
    name = models.CharField(max_length = 20)
    ## one to many relation
    deal = models.ForeignKey(Deal,on_delete = models.CASCADE)
    ## one to one relation
    deal_price = models.OneToOneField(Deal_Items_Price_Lookup,on_delete= models.CASCADE)

    creator_on_prem = models.BooleanField(default= False)
    explorer_on_prem = models.BooleanField(default= False)
    viewer_on_prem = models.BooleanField(default= False)
    term_desktop_personal = models.BooleanField(default= False)
    term_desktop_professional = models.BooleanField(default= False)
    term_server_core = models.BooleanField(default= False)
    term_server_interactor = models.BooleanField(default= False)
    tableau_online = models.BooleanField(default= False)
    server_management = models.BooleanField(default= False)
    creator_online = models.BooleanField(default= False)
    explorer_online = models.BooleanField(default= False)
    viewer_online = models.BooleanField(default= False)
    perpetual_desktop_personal = models.BooleanField(default= False)
    perpetual_desktop_professinal = models.BooleanField(default= False)
    perpetual_server_core = models.BooleanField(default= False)
    perpetual_server_interactor = models.BooleanField(default= False)
    data_management_online = models.BooleanField(default= False)
    data_management_on_premise = models.BooleanField(default= False)
    def __str__(self):
        return self.name
