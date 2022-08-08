# Generated by Django 3.1.7 on 2022-08-08 11:46

from django.db import migrations, models
import django.db.models.deletion
import musics.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('artiste', models.CharField(max_length=500)),
                ('time_length', models.DecimalField(blank=True, decimal_places=2, max_digits=20)),
                ('audio_file', models.FileField(upload_to='musics/', validators=[musics.validators.validate_is_audio])),
                ('cover_image', models.ImageField(upload_to='music_images/')),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='musics.album')),
            ],
        ),
    ]
