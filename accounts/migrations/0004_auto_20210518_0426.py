# Generated by Django 3.1.7 on 2021-05-17 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210517_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='profile1.png', upload_to='pics', verbose_name='Your Photo'),
        ),
    ]
