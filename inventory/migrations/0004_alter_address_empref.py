# Generated by Django 4.1.7 on 2023-03-09 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_address_empref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='empref',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='inventory.employee'),
        ),
    ]