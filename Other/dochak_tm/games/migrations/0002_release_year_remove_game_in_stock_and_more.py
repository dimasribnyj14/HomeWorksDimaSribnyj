# Generated by Django 4.1.6 on 2023-02-27 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Release_Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='in_stock',
        ),
        migrations.RemoveField(
            model_name='game',
            name='last_updated',
        ),
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(upload_to='gamesimage'),
        ),
        migrations.AlterField(
            model_name='game',
            name='release_date',
            field=models.CharField(max_length=255),
        ),
    ]
