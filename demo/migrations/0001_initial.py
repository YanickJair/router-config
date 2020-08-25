# Generated by Django 3.1 on 2020-08-24 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('layout', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50, unique=True, verbose_name='IP')),
                ('hostname', models.CharField(max_length=50, unique=True, verbose_name='Hostname')),
                ('client_name', models.CharField(max_length=50, verbose_name='Cliente')),
                ('address', models.CharField(max_length=50, verbose_name='Morada')),
                ('technician_contact', models.CharField(max_length=50, verbose_name='Contacto Técnico')),
                ('router', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='demo.router')),
            ],
        ),
    ]
