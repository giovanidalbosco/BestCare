# Generated by Django 4.1 on 2022-10-20 17:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade_nome', models.CharField(default='', max_length=100, verbose_name='Cidade')),
                ('cidade_uf', models.CharField(default='', max_length=2, verbose_name='UF')),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
                'ordering': ['cidade_nome'],
            },
        ),
        migrations.CreateModel(
            name='Comorbidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comorbidade_nome', models.CharField(default='', max_length=50, verbose_name='Comorbidade')),
            ],
            options={
                'verbose_name': 'Comorbidade',
                'verbose_name_plural': 'Comorbidades',
                'ordering': ['comorbidade_nome'],
            },
        ),
        migrations.CreateModel(
            name='Medicamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicamento_nome', models.CharField(default='', max_length=50, verbose_name='Medicamento')),
                ('medicamento_fabricante', models.CharField(default='', max_length=50, verbose_name='Fabricante')),
                ('medicamento_apresentacao', models.IntegerField(choices=[(1, 'Comprimido'), (2, 'Dragea'), (3, 'Gota'), (4, 'Injetavel'), (5, 'Ampola'), (6, 'Bisnaga'), (7, 'Unidade'), (8, 'Adesivo'), (9, 'Aerosol'), (10, 'Bolsa'), (11, 'Capsula'), (12, 'Colirio'), (13, 'Creme'), (14, 'Envelope'), (15, 'Inalatorio'), (16, 'Injetavel UI'), (17, 'Pilula'), (18, 'Pomada'), (19, 'Sache'), (20, 'Seringa'), (21, 'Shampoo'), (22, 'Solucao Gotas'), (23, 'Solucao ML'), (24, 'Solucao UI'), (25, 'Suspencao'), (26, 'Xarope'), (27, 'Tablete')], default=None, verbose_name='Apresentacao')),
                ('medicamento_via', models.IntegerField(choices=[(1, 'Oral'), (2, 'Intra-Venoso'), (3, 'Nasal'), (4, 'Ocular'), (5, 'Intramuscular'), (6, 'Topico'), (7, 'Nebulizacao'), (8, 'Otologica'), (9, 'Retal'), (10, 'Sonda-Nasoenteral'), (11, 'Gastrostomia'), (12, 'Sub-cutanea'), (13, 'Sub-lingual'), (14, 'Vaginal')], default=None)),
            ],
            options={
                'verbose_name': 'Medicamentos',
                'ordering': ['medicamento_nome'],
            },
        ),
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoa_nome', models.CharField(max_length=50, unique=True, verbose_name='Nome')),
                ('pessoa_endereco', models.CharField(blank=True, max_length=100, null=True, verbose_name='Endereco')),
                ('pessoa_numero', models.CharField(blank=True, max_length=10, null=True, verbose_name='Numero')),
                ('pessoa_compl', models.CharField(blank=True, max_length=30, null=True, verbose_name='Complemento')),
                ('pessoa_CEP', models.CharField(blank=True, max_length=10, null=True, verbose_name='CEP')),
                ('pessoa_CPF', models.CharField(max_length=14, unique=True, verbose_name='CPF')),
                ('pessoa_classe', models.IntegerField(choices=[(1, 'Cuidador'), (2, 'Residente'), (3, 'Responsavel')])),
                ('pessoa_telefone', models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='Telefone')),
                ('pessoa_email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='E-mail')),
                ('pessoa_plano', models.IntegerField(blank=True, choices=[(1, 'PARTICULAR'), (2, 'SUS'), (3, 'CONVENIO')], null=True)),
                ('pessoa_cidade', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app1.cidades', verbose_name='Cidade')),
                ('pessoa_comorbidade', models.ManyToManyField(to='app1.comorbidades', verbose_name='Comorbidades')),
                ('pessoa_responsavel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.pessoas', verbose_name='Responsável')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
                'ordering': ['pessoa_nome'],
            },
        ),
        migrations.CreateModel(
            name='SinalVital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sinalVitalCreate', models.DateTimeField(auto_now_add=True, verbose_name='TimeStamp')),
                ('sinalVital_pas', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(240), django.core.validators.MinValueValidator(60)], verbose_name='P.A. Sistolica')),
                ('sinalVital_pad', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(160), django.core.validators.MinValueValidator(40)], verbose_name='P.A. Diastolica')),
                ('sinalVital_fc', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(240), django.core.validators.MinValueValidator(60)], verbose_name='Frequencia Cardiaca')),
                ('sinalVital_fr', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(12)], verbose_name='Frequencia Respiratoria')),
                ('sinalVital_temp', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(43.0), django.core.validators.MinValueValidator(33.0)], verbose_name='Temperatura')),
                ('sinalVital_peso', models.FloatField(default=0, verbose_name='Peso')),
                ('sinalVital_altura', models.FloatField(default=0, verbose_name='Altura')),
                ('sinalVital_IMC', models.FloatField(default=0, verbose_name='IMC')),
                ('sinalVital_pessoa_nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.pessoas', verbose_name='Residente')),
            ],
            options={
                'verbose_name': 'Sinal Vital',
                'verbose_name_plural': 'Sinais Vitais',
                'ordering': ['-sinalVitalCreate'],
            },
        ),
        migrations.CreateModel(
            name='Ocorrencias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocorrencia_nome', models.IntegerField(choices=[(1, 'Agressividade'), (2, 'Alteracoes Glicemia'), (3, 'Cefaleia'), (4, 'Convulcao'), (5, 'Cuidado Paliativo'), (6, 'Deficit Motor'), (7, 'Desidratacao'), (8, 'Desnutricao'), (9, 'Diarreia'), (10, 'Doencas Respiratorias'), (11, 'Dor Abdominal'), (12, 'Dor Epigastrica'), (13, 'dor Torassica'), (14, 'Entorce'), (15, 'Escabiose'), (16, 'Febre'), (17, 'FR Alterada'), (18, 'Ematoma'), (19, 'Infeccao TRato Urinario'), (20, 'Internacao'), (21, 'Lesao de Pele'), (22, 'Liberacao de Cateteres e Sondas'), (23, 'Modificacao de Prescricao'), (24, 'Neutropenia Febril'), (25, 'Obito'), (26, 'PA Alterada'), (27, 'Queda'), (28, 'Retirada de Dispositivo')], default='', verbose_name='Ocorrencia')),
                ('ocorrencia_observacao', models.TextField(blank=True, verbose_name='Observação')),
                ('ocorrencia_pessoa_cuidador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='app1.pessoas', verbose_name='Cuidador')),
                ('ocorrencia_pessoa_nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.pessoas', verbose_name='Residente')),
            ],
            options={
                'verbose_name': 'Ocorrencia',
                'verbose_name_plural': 'Ocorrencias',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.IntegerField(choices=[(1, 'Medicamento'), (2, 'Consulta Medica'), (3, 'Fisioterapia'), (4, 'Atividade Fisica'), (5, 'Atividade Cultural'), (6, 'Atividade Recreativa')], default='', verbose_name='Evento')),
                ('event_dose', models.IntegerField(choices=[(1, '1/4'), (2, '1/2'), (3, '3/4'), (4, '1'), (5, '1 + 1/4'), (6, '1 + 1/2'), (7, '1 + 3/4')], default=0, verbose_name='Dose')),
                ('description', models.TextField(verbose_name='Descricao')),
                ('status', models.BooleanField(default=False, verbose_name='Concluído?')),
                ('start_time', models.DateTimeField(verbose_name='Dia/Hora - Inicio')),
                ('end_time', models.DateTimeField(verbose_name='Dia/Hora - Fim')),
                ('event_consumo_nome', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app1.medicamentos', verbose_name='Medicamento')),
                ('event_pessoa_nome', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app1.pessoas', verbose_name='Residente')),
            ],
        ),
        migrations.CreateModel(
            name='Estoque_Individual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estoqueCreate', models.DateTimeField(auto_now_add=True, verbose_name='TimeStamp')),
                ('estoque_movimento', models.CharField(choices=[(1, 'Entrada'), (2, 'Saida')], default='', max_length=1)),
                ('estoque_quantidade', models.IntegerField(default=0, verbose_name='Quantidade')),
                ('estoque_saldo', models.IntegerField(default=0, verbose_name='Saldo em Estoque')),
                ('estoque_pessoa_nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.pessoas', verbose_name='Residente')),
                ('estoque_usos_consumo', models.ManyToManyField(to='app1.medicamentos', verbose_name='Produto')),
            ],
            options={
                'verbose_name': 'Estoque Individual',
                'verbose_name_plural': 'Estoque Individuais',
            },
        ),
    ]
