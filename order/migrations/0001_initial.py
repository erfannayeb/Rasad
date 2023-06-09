# Generated by Django 3.2.8 on 2022-01-29 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(blank=True, null=True)),
                ('state', models.CharField(choices=[('p', 'pending'), ('i', 'in-progress'), ('d', 'delivered'), ('r', 'returned'), ('c', 'canceled')], max_length=1)),
                ('deliverMethod', models.CharField(choices=[('e', 'express'), ('p', 'post')], max_length=1)),
                ('paymentMethod', models.CharField(choices=[('o', 'online'), ('c', 'cash')], max_length=1)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('items', models.ManyToManyField(blank=True, null=True, related_name='items', to='cart.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
