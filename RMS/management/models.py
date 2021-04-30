from django.db import models
from django.utils import timezone
from datetime import datetime

COLOR_CHOICES = (
    ('general','GENERAL'),
    ('ladies', 'LADIES'),
    ('tatkal','TATKAL'),
    ('premiumtatkal','PREMIUM TATKAL'),
)

class Booking(models.Model):  
    name = models.CharField(max_length=20)  
    age = models.IntegerField(default=0,null=True)  
    abtu = models.CharField(max_length=300)  
    typclass= models.CharField(max_length=20)
    typconcession = models.CharField(max_length=20, choices=COLOR_CHOICES, default='general')

    roundtrip = models.BooleanField(default=False)
    datefortrip = models.DateField(default=datetime.now)
    images = models.ImageField(upload_to='pics',default='None',null=True)

    # typway = models.CharField(max_length=20,blank=True)  
    # date = models.CharField(max_length=100,blank=True)

    class Meta:  
        db_table = "booking"