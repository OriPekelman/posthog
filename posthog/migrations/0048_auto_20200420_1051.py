# Generated by Django 3.0.3 on 2020-04-20 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posthog', '0047_auto_20200416_1631'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='event',
            name='posthog_eve_timesta_b00cec_idx',
        ),
        migrations.AddIndex(
            model_name='event',
            index=models.Index(fields=['timestamp', 'team_id', 'event'], name='posthog_eve_timesta_1f6a8c_idx'),
        ),
    ]
