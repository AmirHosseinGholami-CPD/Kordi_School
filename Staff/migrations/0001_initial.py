# Generated by Django 5.0.7 on 2024-09-20 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=100)),
                ('staff', models.CharField(max_length=120)),
                ('phone_number', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='photos/')),
            ],
        ),
    ]
