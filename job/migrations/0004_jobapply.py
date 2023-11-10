# Generated by Django 4.2.6 on 2023-11-07 23:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_category_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('Link_url', models.URLField(blank=True, help_text='please enter your linkedin profile url', null=True)),
                ('github_url', models.URLField(blank=True, help_text='please enter your github profile url', null=True)),
                ('cv', models.FileField(help_text='please upload your latest cv', upload_to='cv')),
                ('cover_letter', models.TextField(help_text='add your nodes here....', max_length=500)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply_job', to='job.job')),
            ],
        ),
    ]