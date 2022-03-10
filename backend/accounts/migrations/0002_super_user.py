# Generated by Django 4.0.3 on 2022-03-10 12:18
import os

from django.db import migrations


def generate_superuser(apps, schema_editor):
    User = apps.get_model('accounts', 'CustomUser')

    DJANGO_SU_NAME = os.environ.get('DJANGO_SU_NAME')
    DJANGO_SU_EMAIL = os.environ.get('DJANGO_SU_EMAIL')
    DJANGO_SU_PASSWORD = os.environ.get('DJANGO_SU_PASSWORD')

    User.objects.create_superuser(
        username=DJANGO_SU_NAME,
        email=DJANGO_SU_EMAIL,
        password=DJANGO_SU_PASSWORD
    )


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(generate_superuser)
    ]
