# Generated by Django 4.1.6 on 2023-02-03 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='participation',
            name='Person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='participation',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event'),
        ),
        migrations.AddField(
            model_name='event',
            name='organise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='participations',
            field=models.ManyToManyField(related_name='participations', through='events.Participation', to=settings.AUTH_USER_MODEL),
        ),
    ]
