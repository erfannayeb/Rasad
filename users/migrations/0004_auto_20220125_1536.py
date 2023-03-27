# Generated by Django 3.2.8 on 2022-01-25 12:06

from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('users', '0003_auto_20220125_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='companies', to='category.category'),
        ),
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=users.models.company_image_path),
        ),
    ]