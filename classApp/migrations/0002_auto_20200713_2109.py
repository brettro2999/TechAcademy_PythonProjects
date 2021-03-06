# Generated by Django 3.0.8 on 2020-07-14 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangoclasses',
            name='course',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='djangoclasses',
            name='duration',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=1000),
        ),
        migrations.AlterField(
            model_name='djangoclasses',
            name='instructor',
            field=models.CharField(default='', max_length=60),
        ),
    ]
