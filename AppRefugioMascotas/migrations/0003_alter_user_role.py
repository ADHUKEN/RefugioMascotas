# Generated by Django 4.0.3 on 2022-04-15 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppRefugioMascotas', '0002_user_image_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Administrador'), ('colab', 'Colaborador'), ('client', 'Cliente')], default='client', max_length=300),
        ),
    ]