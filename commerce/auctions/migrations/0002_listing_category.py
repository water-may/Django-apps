# Generated by Django 4.1.1 on 2022-09-30 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
