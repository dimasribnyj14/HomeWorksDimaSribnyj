# Generated by Django 4.1 on 2023-02-12 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ForumApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
