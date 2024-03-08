# Generated by Django 5.0.1 on 2024-01-09 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=80)),
                ('Author', models.CharField(max_length=80)),
                ('ISBN', models.IntegerField()),
                ('Genre', models.CharField(max_length=80)),
                ('Publication_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('borrowed_books', models.ManyToManyField(blank=True, related_name='borrowed_by', to='lmsapp.book')),
            ],
        ),
    ]
