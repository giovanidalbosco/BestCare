# Generated by Django 4.1 on 2022-10-10 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_sinalvital_sinalvital_altura_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinalvital',
            name='sinalVital_IMC',
            field=models.FloatField(default=0, verbose_name='IMC'),
        ),
    ]