# Generated by Django 5.1.3 on 2024-11-12 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_ong_latitude_alter_ong_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ong',
            name='imagem',
            field=models.CharField(blank=True, default='imagens/rick_roll.jpg', max_length=1000, null=True),
        ),
    ]
