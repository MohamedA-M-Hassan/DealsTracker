# Generated by Django 2.1.1 on 2020-02-13 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal_app', '0003_deal_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]