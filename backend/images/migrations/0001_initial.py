# Generated by Django 4.0.3 on 2022-03-11 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import images.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.FileField(upload_to='images_files/', validators=[images.validators.validate_file_type])),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.FileField(upload_to='resized_images')),
                ('height', models.PositiveIntegerField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thumbnails', to='images.image')),
            ],
        ),
    ]
