# Generated by Django 4.1 on 2022-12-26 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_stands', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cookiestand',
            name='average_cookies_per_sale',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cookiestand',
            name='hourly_sales',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AddField(
            model_name='cookiestand',
            name='maximum_customers_per_hour',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cookiestand',
            name='minimum_customers_per_hour',
            field=models.IntegerField(default=0),
        ),
    ]
