# Generated by Django 2.2.6 on 2022-05-31 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='titulo',
            field=models.CharField(default='Title', max_length=50),
        ),
    ]
