from django.db import models

class File(models.Model):
    file = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.file.name

class Foo(models.Model):
    fubar = models.TextField()


class Row(models.Model):
    Observation_Date = models.CharField(max_length=100)
    Retail_Sales_Volume = models.FloatField(max_length=100, default = 0)
    Retail_Price = models.FloatField(max_length=100, default = 0)
    Acv_Distribution =models.FloatField(max_length=100, default = 0)
    Competition = models.FloatField(max_length=100, default = 0)
    Edlp = models.FloatField(max_length=100, default = 0)
    Trade_Any_Promo = models.FloatField(max_length=100, default = 0)
    Tv = models.FloatField(max_length=100, default = 0)
    Print_Ad = models.FloatField(max_length=100, default = 0)
    Online_Display = models.FloatField(max_length=100, default = 0)
    Preroll_Video = models.FloatField(max_length=100, default = 0)
    Paid_Search = models.FloatField(max_length=100, default = 0)
    Public_Relations = models.FloatField(max_length=100, default = 0)
    Fsi = models.FloatField(max_length=100, default = 0)
    Digital_Coupon = models.FloatField(max_length=100, default = 0)
    Shopper_Marketing = models.FloatField(max_length=100, default = 0)

    





