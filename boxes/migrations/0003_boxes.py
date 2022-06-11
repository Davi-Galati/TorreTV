# Generated by Django 2.2.6 on 2022-05-31 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxes', '0002_auto_20220531_0732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boxes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_box', models.CharField(max_length=150)),
                ('bloco', models.CharField(max_length=10)),
                ('nome_responsavel', models.TextField()),
                ('numero_loja', models.IntegerField()),
                ('descricao', models.TextField()),
                ('foto_boxes', models.ImageField(blank=True, upload_to='fotos_boxes/%d/%m/%Y')),
            ],
        ),
    ]
