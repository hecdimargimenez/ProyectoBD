# Generated by Django 4.0.3 on 2022-04-20 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SistemaGarantiaApp', '0002_alter_departamento_codigo_dpto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='img_prod',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
    ]
