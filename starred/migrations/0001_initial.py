# Generated by Django 3.1 on 2023-06-10 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0002_auto_20230601_0938'),
        ('documents', '0004_auto_20230607_0709'),
        ('music', '0002_auto_20230601_0938'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0002_auto_20230601_0938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Starred',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.document')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='images.images')),
                ('music', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.music')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='videos.videos')),
            ],
        ),
    ]