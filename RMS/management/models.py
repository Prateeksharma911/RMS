from django.db import models
from django.utils import timezone
from datetime import datetime

COLOR_CHOICES = (
    ('general','GENERAL'),
    ('ladies', 'LADIES'),
    ('tatkal','TATKAL'),
    ('premiumtatkal','PREMIUM TATKAL'),
)
CONCESSION_CHOICES = (
    ('AC First Class','AC First Class'),
    ('AC 2-Tier', 'AC 2-Tier'),
    ('AC 3-Tier', 'AC 3-Tier'),
    ('First Class', 'First Class'),
    )

class Booking(models.Model):  
    name = models.CharField(max_length=20)  
    age = models.IntegerField(default=0,null=True)  
    abtu = models.CharField(max_length=300)  
    typclass= models.CharField(max_length=30,choices=CONCESSION_CHOICES, default='AC First Class')
    typconcession = models.CharField(max_length=20, choices=COLOR_CHOICES, default='general')
    cost = models.FloatField()

    roundtrip = models.BooleanField(default=False)
    datefortrip = models.DateField(default=datetime.now)
    images = models.ImageField(upload_to='pics',default='None',null=True)

    class Meta:  
        db_table = "booking"