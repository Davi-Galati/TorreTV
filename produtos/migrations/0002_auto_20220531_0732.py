# Generated by Django 2.2.6 on 2022-05-31 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boxes', '0002_auto_20220531_0732'),
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Produtos',
            new_name='Produto',
        ),
    ]
