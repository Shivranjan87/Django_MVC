# Generated by Django 4.1.7 on 2023-03-16 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='tqual',
            field=models.CharField(choices=[('BE', 'Bachelor of Engineering'), ('ME', 'Masters of Engineering'), ('MCA', 'Masters of Computer Applications'), ('M.Pharm', 'Masters of Pharmacy')], max_length=40),
        ),
        migrations.AlterModelTable(
            name='teacher',
            table='Teacher_Abstract',
        ),
    ]
