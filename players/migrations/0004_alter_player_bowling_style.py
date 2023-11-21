# Generated by Django 4.2.7 on 2023-11-21 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_remove_player_position_player_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='bowling_style',
            field=models.CharField(blank=True, choices=[('Right-arm fast', 'Right-arm fast'), ('Left-arm fast', 'Left-arm fast'), ('Left-arm medium', 'Left-arm medium'), ('Right-arm medium', 'Right-arm medium'), ('Left-arm spin', 'Left-arm spin'), ('Right-arm spin', 'Right-arm spin'), ('not-a-Bowler', 'not-a-Bowler')], max_length=255, null=True),
        ),
    ]
