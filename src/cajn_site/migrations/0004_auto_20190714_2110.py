# Generated by Django 2.2.2 on 2019-07-15 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cajn_site', '0003_auto_20190710_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='vehicles',
            field=models.ManyToManyField(blank=True, to='cajn_site.Vehicle'),
        ),
    ]