# Generated by Django 4.0.3 on 2022-04-15 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppRefugioMascotas', '0003_alter_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_customer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_employee',
        ),
    ]