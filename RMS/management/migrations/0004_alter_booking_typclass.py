# Generated by Django 3.2 on 2021-04-30 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_alter_booking_typclass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='typclass',
            field=models.CharField(choices=[('AC First Class', 'AC First Class'), ('AC 2-Tier', 'AC 2-Tier'), ('AC 3-Tier', 'AC 3-Tier'), ('First Class', 'First Class')], default='AC First Class', max_length=30),
        ),
    ]
