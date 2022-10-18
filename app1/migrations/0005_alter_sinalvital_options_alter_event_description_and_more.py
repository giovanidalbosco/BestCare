# Generated by Django 4.1 on 2022-10-13 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_medicamentos_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sinalvital',
            options={'ordering': ['-sinalVitalCreate'], 'verbose_name': 'Sinal Vital', 'verbose_name_plural': 'Sinais Vitais'},
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(verbose_name='Descricao'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(verbose_name='Dia/Hora - Fim'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_consumo_nome',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app1.medicamentos', verbose_name='Medicamento'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_dose',
            field=models.IntegerField(choices=[(1, '1/4'), (2, '1/2'), (3, '3/4'), (4, '1'), (5, '1 + 1/4'), (6, '1 + 1/2'), (7, '1 + 3/4')], default=0, verbose_name='Dose'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(verbose_name='Dia/Hora - Inicio'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.IntegerField(choices=[(1, 'Medicamento'), (2, 'Consulta Medica'), (3, 'Fisioterapia'), (4, 'Atividade Fisica'), (5, 'Atividade Cultural'), (6, 'Atividade Recreativa')], default='', verbose_name='Evento'),
        ),
        migrations.AlterField(
            model_name='sinalvital',
            name='sinalVital_fc',
            field=models.CharField(default='', max_length=5, verbose_name='Frequencia Cardiaca'),
        ),
        migrations.AlterField(
            model_name='sinalvital',
            name='sinalVital_fr',
            field=models.CharField(default='', max_length=5, verbose_name='Frequencia Respiratoria'),
        ),
        migrations.AlterField(
            model_name='sinalvital',
            name='sinalVital_pad',
            field=models.CharField(default='', max_length=5, verbose_name='P.A. Diastolica'),
        ),
        migrations.AlterField(
            model_name='sinalvital',
            name='sinalVital_pas',
            field=models.CharField(default='', max_length=5, verbose_name='P.A. Sistolica'),
        ),
        migrations.AlterField(
            model_name='sinalvital',
            name='sinalVital_temp',
            field=models.CharField(default='', max_length=5, verbose_name='Temperatura'),
        ),
    ]