# Generated by Django 5.0.7 on 2024-08-31 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amadegi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Arabic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Emla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='English',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Farhang_Honar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Farsi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Fizik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Kar_Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Maref',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Math',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Motaleat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Negaresh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Quran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shimi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Varzesh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Zist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
            ],
        ),
    ]
