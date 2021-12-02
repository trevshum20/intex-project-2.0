# Generated by Django 3.2.8 on 2021-12-02 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drugname', models.CharField(max_length=255, null=True)),
                ('isopioid', models.BooleanField(verbose_name='Opioid')),
                ('avg', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'drug',
            },
        ),
        migrations.CreateModel(
            name='pd_statedata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=20, null=True)),
                ('stateabbrev', models.CharField(max_length=2, null=True)),
                ('population', models.IntegerField(null=True)),
                ('deaths', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'pd_statedata',
            },
        ),
        migrations.CreateModel(
            name='Prescriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50, null=True)),
                ('lname', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(max_length=1, null=True)),
                ('state', models.CharField(max_length=2, null=True)),
                ('credential', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'prescriber',
            },
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty', models.CharField(max_length=255, null=True)),
                ('weight', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'specialty',
            },
        ),
        migrations.CreateModel(
            name='Prescriber_Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Opioids.drug')),
                ('prescriber', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Opioids.prescriber')),
            ],
            options={
                'db_table': 'prescriber_drug',
            },
        ),
        migrations.AddField(
            model_name='prescriber',
            name='specialty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Opioids.specialty'),
        ),
    ]