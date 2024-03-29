# Generated by Django 5.0.2 on 2024-03-21 16:44

import datetime
import recordatorios.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordatorios', '0010_alter_evento_fecha_alter_evento_recordatorio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('etiqueta', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha',
            field=models.DateField(default=datetime.date(2024, 3, 22), validators=[recordatorios.models.fecha_limite_mayor_que_hoy]),
        ),
        migrations.AlterField(
            model_name='evento',
            name='recordatorio',
            field=models.DateField(default=datetime.date(2024, 3, 22), validators=[recordatorios.models.fecha_recordatorio_mayor_que_hoy]),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fecha_pago',
            field=models.DateField(default=datetime.date(2024, 3, 22), validators=[recordatorios.models.fecha_limite_mayor_que_hoy]),
        ),
        migrations.AlterField(
            model_name='pago',
            name='recordatorio',
            field=models.DateField(default=datetime.date(2024, 3, 22), validators=[recordatorios.models.fecha_recordatorio_mayor_que_hoy]),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='fecha_limite',
            field=models.DateField(default=datetime.date(2024, 3, 22), validators=[recordatorios.models.fecha_limite_mayor_que_hoy]),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='recordatorio',
            field=models.DateField(default=datetime.date(2024, 3, 22), validators=[recordatorios.models.fecha_recordatorio_mayor_que_hoy]),
        ),
    ]
