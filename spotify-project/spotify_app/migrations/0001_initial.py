# Generated by Django 5.0.3 on 2024-04-01 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SongCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songTitle', models.TextField()),
                ('songArtist', models.TextField()),
                ('songThumbnail', models.TextField()),
            ],
        ),
    ]
