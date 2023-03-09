# Generated by Django 4.1.7 on 2023-03-07 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('numofbooks', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=40)),
            ],
            options={
                'db_table': 'AUTHOR_MASTER',
            },
        ),
        migrations.CreateModel(
            name='CustomerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=45)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=40)),
            ],
            options={
                'db_table': 'USER_CUSTOMER_MASTER',
            },
        ),
        migrations.CreateModel(
            name='PersonInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=45)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=40)),
            ],
            options={
                'db_table': 'PERSON_MASTER',
            },
        ),
    ]