# Generated by Django 4.2.6 on 2023-10-31 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_slug_alter_job_vacancy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='logo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
