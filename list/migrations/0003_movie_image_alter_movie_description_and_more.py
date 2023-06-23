# Generated by Django 4.2.2 on 2023-06-23 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_movie_description_long_alter_movie_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.CharField(default='tmp url', max_length=512),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description_long',
            field=models.CharField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=1028),
        ),
    ]
