# Generated by Django 4.0.6 on 2022-07-16 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auction', '0003_alter_auction_enddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='startprice',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]