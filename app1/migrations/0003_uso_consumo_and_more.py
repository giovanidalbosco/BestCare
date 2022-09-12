# Generated by Django 4.1 on 2022-09-09 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_prescricao_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uso_Consumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumo_nome', models.CharField(default='', max_length=50, verbose_name='Uso e consumo')),
                ('consumo_fabricante', models.CharField(default='', max_length=50, verbose_name='Fabricante')),
                ('consumo_apresentacao', models.CharField(choices=[('1', 'Comprimido'), ('2', 'Dragea'), ('3', 'Gota'), ('4', 'Injetavel'), ('5', 'Ampola'), ('6', 'Bisnaga'), ('7', 'Unidade')], default='', max_length=1, verbose_name='Apresentacao')),
                ('consumo_via', models.CharField(choices=[('1', 'Oral'), ('2', 'Intra-Venoso'), ('3', 'Nasal'), ('4', 'Ocular')], default='', max_length=1)),
            ],
            options={
                'verbose_name': 'Uso e consumo',
                'ordering': ['consumo_nome'],
            },
        ),
        migrations.AlterField(
            model_name='estoque_individual',
            name='estoque_usos_consumo',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='app1.uso_consumo', verbose_name='Produto'),
        ),
        migrations.AlterField(
            model_name='prescricao',
            name='prescricao_consumo_nome',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app1.uso_consumo', verbose_name='Produto'),
        ),
        migrations.DeleteModel(
            name='Usos_Consumo',
        ),
    ]