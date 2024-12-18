# Generated by Django 5.1.3 on 2024-11-26 16:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_ong_imagem_avaliacaoong'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Armazenamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_tecido', models.CharField(max_length=100)),
                ('metros', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.ong')),
            ],
        ),
        migrations.CreateModel(
            name='EditarAvaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='editar_avaliacoes', to='usuarios.ong')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='editar_avaliacoes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('ong', 'usuario')},
            },
        ),
        migrations.CreateModel(
            name='RemoverAvaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remover_avaliacoes', to='usuarios.ong')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remover_avaliacoes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('ong', 'usuario')},
            },
        ),
    ]
