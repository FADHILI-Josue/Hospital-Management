# Generated by Django 4.2.9 on 2024-01-11 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_specialty_alter_doctors_specialty'),
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Time',
                'verbose_name_plural': 'Times',
            },
        ),
        migrations.AlterModelOptions(
            name='appointment',
            options={'verbose_name': 'Appointment', 'verbose_name_plural': 'Appointments'},
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='patient_id',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='start_time',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.doctors'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.patients'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='patients.time'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.status'),
        ),
    ]