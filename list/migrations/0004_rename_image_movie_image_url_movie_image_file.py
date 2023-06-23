# Generated by Django 4.2.2 on 2023-06-23 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_movie_image_alter_movie_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='image',
            new_name='image_url',
        ),
        migrations.AddField(
            model_name='movie',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
