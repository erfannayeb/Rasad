# Generated by Django 3.2.8 on 2022-01-25 09:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=60, null=True, unique=True)),
                ('phone_number', models.CharField(max_length=15, null=True, unique=True, validators=[users.models.phone_validate])),
                ('password', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(8)])),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_active', models.BooleanField(default=True)),
                ('user_type', models.CharField(choices=[('B', 'Boss'), ('V', 'Visitor'), ('C', 'Customer')], default='B', max_length=1)),
                ('boss_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='visitors', to='users.customuser')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
                'ordering': ['-date_joined'],
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('boss_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customuser')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center', models.FloatField()),
                ('radius', models.FloatField()),
                ('path', models.FloatField(blank=True, default=0, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('boss_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='users.customuser')),
                ('visitor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignee', to='users.customuser')),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
            },
        ),
    ]
