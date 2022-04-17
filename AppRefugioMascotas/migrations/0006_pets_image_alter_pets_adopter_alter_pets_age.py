# Generated by Django 4.0.3 on 2022-04-15 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppRefugioMascotas', '0005_pets'),
    ]

    operations = [
        migrations.AddField(
            model_name='pets',
            name='image',
            field=models.ImageField(default='pet.jpg', upload_to='pet_pics'),
        ),
        migrations.AlterField(
            model_name='pets',
            name='adopter',
            field=models.ForeignKey(blank=True, default='Disponible', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Adoptante'),
        ),
        migrations.AlterField(
            model_name='pets',
            name='age',
            field=models.IntegerField(max_length=5, verbose_name='Edad'),
        ),
    ]
