# Generated by Django 4.1 on 2022-09-24 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_pessoas_pessoa_comorbidade_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoas',
            name='pessoa_comorbidade',
        ),
        migrations.AddField(
            model_name='pessoas',
            name='pessoa_comorbidade',
            field=models.ManyToManyField(to='app1.comorbidades', verbose_name='Comorbidades'),
        ),
    ]
