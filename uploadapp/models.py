from django.db import models

class File(models.Model):
    file = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.file.name

class Foo(models.Model):
    fubar = models.TextField()


class Row(models.Model):
    Observation_Date = models.CharField(max_length=10)
    Retail_Sales_Volume = models.FloatField(default = 0)
    Retail_Price = models.FloatField(default = 0)
    Acv_Distribution =models.FloatField(default = 0)
    Competition = models.FloatField(default = 0)
    Edlp = models.FloatField(default = 0)
    Trade_Any_Promo = models.FloatField(default = 0)
    Tv = models.FloatField(default = 0)
    Print_Ad = models.FloatField(default = 0)
    Online_Display = models.FloatField(default = 0)
    Preroll_Video = models.FloatField(default = 0)
    Paid_Search = models.FloatField(default = 0)
    Public_Relations = models.FloatField(default = 0)
    Fsi = models.FloatField(default = 0)
    Digital_Coupon = models.FloatField(default = 0)
    Shopper_Marketing = models.FloatField(default = 0)

    





