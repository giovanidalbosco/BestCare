# Generated by Django 4.1 on 2022-10-19 22:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_sinalvital_sinalvital_fc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Concluído?'),
        ),
        migrations.AddField(
            model_name='pessoas',
            name='pessoa_responsavel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.pessoas', verbose_name='Responsável'),
        ),
        migrations.AlterField(
            model_name='sinalvital',
            name='sinalVital_fc',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(240), django.core.validators.MinValueValidator(60)], verbose_name='Frequencia Cardiaca'),
        ),
        migrations.AlterField(
            model_name='sinalvital',
            name='sinalVital_fr',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(12)], verbose_name='Frequencia Respiratoria'),
        ),
        migrations.AlterField(
            model_name='sinalvital',
            name='sinalVital_pad',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(160), django.core.validators.MinValueValidator(40)], verbose_name='P.A. Diastolica'),
        ),
        migrations.AlterField(
            model_name='sinalvital',
            name='sinalVital_temp',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(43.0), django.core.validators.MinValueValidator(33.0)], verbose_name='Temperatura'),
        ),
    ]
