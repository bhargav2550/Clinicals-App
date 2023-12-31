# Generated by Django 4.1.7 on 2023-04-10 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LastName', models.CharField(max_length=20)),
                ('FirstName', models.CharField(max_length=20)),
                ('Age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Clinicaldata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ComponentName', models.CharField(choices=[('hw', 'Height/Weight'), ('bp', 'Blood Pressure'), ('heartrate', 'HeartRate')], max_length=20)),
                ('componentValue', models.CharField(max_length=20)),
                ('MeasureDateTime', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinicalsApp.patient')),
            ],
        ),
    ]
