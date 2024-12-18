# Generated by Django 5.1.3 on 2024-11-07 23:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ONG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='ONG', max_length=255)),
                ('cnpj', models.CharField(default='00.000.000/0001-00', max_length=18)),
                ('endereco', models.CharField(default='Rua', max_length=255)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('informacao', models.TextField(blank=True, null=True)),
                ('imagem', models.CharField(blank=True, default='imagens/rick_roll.jpg', max_length=100, null=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ong', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Residuos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('quantidade', models.IntegerField()),
                ('peso', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(choices=[('armazenado', 'Armazenado'), ('reciclado', 'Reciclado'), ('descartado', 'Descartado')], max_length=50)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('ong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residuos', to='usuarios.ong')),
            ],
        ),
    ]
