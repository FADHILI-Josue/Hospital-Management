# Generated by Django 4.2.9 on 2024-01-11 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_alter_blogs_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='blogs/thumbnail'),
        ),
    ]