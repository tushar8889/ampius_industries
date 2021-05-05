from django.db import models

# Create your models here.

class FarmDetail(models.Model):
    field_id = models.CharField(max_length=100, default=0)
    username = models.CharField(max_length=100, default=0)
    commodity = models.CharField(max_length=100,default=0)
    sowing_date = models.CharField(max_length=100,default=0)
    field_map = models.CharField(max_length=10000,default=0)
    area = models.CharField(max_length=100,default=0)

    def __str__(self):
        return self.field_id