# Generated by Django 4.1.7 on 2023-03-15 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='person_proxy',
            table='persons_proxy',
        ),
    ]