# Generated by Django 4.2.1 on 2023-07-27 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dados', '0022_jogador_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogador',
            name='foto',
            field=models.ImageField(upload_to='jogador_fotos'),
        ),
    ]