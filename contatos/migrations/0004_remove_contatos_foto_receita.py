# Generated by Django 2.2.6 on 2022-06-07 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0003_auto_20220531_0750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contatos',
            name='foto_receita',
        ),
    ]
