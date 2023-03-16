# Generated by Django 4.1.7 on 2023-03-16 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('tid', models.IntegerField()),
                ('tqual', models.CharField(choices=[('BE', 'Bachelor of Engineering'), ('ME', 'Masters of Engineering'), ('MCA', 'Masters of Computer Applications')], max_length=40)),
                ('tsal', models.FloatField()),
            ],
            options={
                'db_table': 'persons_proxy',
            },
        ),
    ]