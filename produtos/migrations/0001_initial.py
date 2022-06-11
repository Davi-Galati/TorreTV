# Generated by Django 2.2.6 on 2022-05-31 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boxes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('foto_produtos', models.ImageField(blank=True, upload_to='fotos_produtos/%d/%m/%Y')),
                ('boxe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boxes.Boxes')),
            ],
        ),
    ]
