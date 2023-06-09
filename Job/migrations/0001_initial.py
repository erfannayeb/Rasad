# Generated by Django 3.2.8 on 2022-01-25 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('salary', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.company')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('resume', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Job.job')),
                ('visitor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customuser')),
            ],
            options={
                'verbose_name': 'Resume',
                'verbose_name_plural': 'Resumes',
            },
        ),
    ]
