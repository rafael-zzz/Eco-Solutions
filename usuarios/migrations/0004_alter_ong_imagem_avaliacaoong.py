# Generated by Django 5.1.3 on 2024-11-23 22:09

import django.db.models.deletion
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
        migrations.CreateModel(
            name='AvaliacaoONG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField()),
                ('ong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to='usuarios.ong')),
            ],
            options={
                'unique_together': {('nota', 'ong')},
            },
        ),
    ]
