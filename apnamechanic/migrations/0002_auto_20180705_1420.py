# Generated by Django 2.0.6 on 2018-07-05 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apnamechanic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MODEL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_in_car', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repair_maintenance', models.CharField(max_length=10, unique=True)),
                ('diagnostics_inspection', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='make_in_car',
            field=models.CharField(choices=[('AU', 'AUDI'), ('BW', 'BMW'), ('HD', 'Honda'), ('NS', 'Nissan')], default=None, max_length=6, unique=True),
        ),
        migrations.AlterField(
            model_name='pincode',
            name='pincode',
            field=models.IntegerField(unique=True),
        ),
        migrations.AddField(
            model_name='model',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='apnamechanic.Car'),
        ),
    ]
