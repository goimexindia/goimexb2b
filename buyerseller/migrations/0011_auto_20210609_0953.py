# Generated by Django 3.1.7 on 2021-06-09 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyerseller', '0010_safedeal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='safedeal',
            name='partnerphone',
            field=models.CharField(default='123456789', max_length=120),
        ),
    ]
